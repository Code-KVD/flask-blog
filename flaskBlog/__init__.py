from flask import Flask
# ORM used to access the database.
from flask_sqlalchemy import SQLAlchemy
# used to encrpt the password of the user.
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.instance_path = 'flaskBlog/instance'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app) 
login_manager.login_view = 'login'

from flaskBlog import routes