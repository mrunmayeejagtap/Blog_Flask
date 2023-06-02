from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config
#from app import create_app


db = SQLAlchemy()

#//todo creates an application context and makes it the current context. This is necessary for certain functionality in Flask to work properly,
#//todo especially when working with databases or other extensions that require access to the Flask application instance. 
#//todo It ensures that the Flask application instance is available to the code that requires it.
#create_app.app_context().push()    #//! Very imp
  
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail()


def create_app(config_class = Config):
    app = Flask(__name__)
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
    app.config.from_object(Config) 

    #print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
