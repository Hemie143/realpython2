# test/test_main.py

import os
import unittest

from chp14_flasktaskr_part07.project import app, db
from chp14_flasktaskr_part07.project._config import basedir
from chp14_flasktaskr_part07.project.models import User

TEST_DB = 'test.db'

class MainTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Helper

    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    # Tests

    def test_404_error(self):
        response = self.app.get('/this-route-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Sorry. There\'s nothing here.', response.data)

    def test_500_error(self):
        bad_user = User('Jeremy', email='jeremy@realpython.com', password='django')
        db.session.add(bad_user)
        db.session.commit()
        self.assertRaises(ValueError, self.login, 'Jeremy', 'django')
        try:
            response = self.login('Jeremy', 'django')
            self.assertEqual(response.status_code, 500)
        except ValueError:
            pass
        # self.assertNotIn(b'ValueError: Invalid salt', response.data)
        # self.assertIn(b'Something went terribly wrong.', response.data)

if __name__ == '__main__':
    unittest.main()
