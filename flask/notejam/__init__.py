from flask import Flask
# import pymysql
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

# @TODO use application factory approach
app = Flask(__name__)

app.config.from_object('notejam.config.Config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

from notejam import views
