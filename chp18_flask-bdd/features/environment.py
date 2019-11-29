import os
import sys
import tempfile

# add module to syspath
# get the current working directory
pwd = os.path.abspath(os.path.dirname(__file__))
# isolate the last folder (the folder we are currently in)
project = os.path.basename(pwd)
# remove the last folder from the cwd
new_path = pwd.strip(project)
# create a new path pointing to where our flask object is defined
full_path = os.path.join(new_path, 'flaskr')

try:
    from flaskr import app, init_db
except ImportError:
    sys.path.append(full_path)
    from flaskr import app, init_db

def before_feature(context, feature):
    app.config['TESTING'] = True
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    context.client = app.test_client()
    init_db()

def after_feature(context, feature):
    os.close(context.db)
    os.unlink(app.config['DATABASE'])

