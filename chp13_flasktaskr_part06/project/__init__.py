# project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from chp13_flasktaskr_part06.project.users.views import users_blueprint
from chp13_flasktaskr_part06.project.tasks.views import tasks_blueprint
# from project.users.views import users_blueprint
# from project.tasks.views import tasks_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)
