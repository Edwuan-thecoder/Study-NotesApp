from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import path to check if a current database exists
from os import path
from flask_login import LoginManager


# Creating SQLAlchemy database
db = SQLAlchemy()
DB_NAME = 'database.db'




def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "eddie"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'

    db.init_app(app)




    # import our views
    from .views import views
    from .auth import auth

    # registering our views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix="/")

    # import table here so that we can define them before  we create our database
    from .models import User, Note, BlogPost

    create_database(app)

    # redirect the User to login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    # figure out why this line is not working!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    login_manager.init_app(app)

    # looking for the Uer table and reference them by their id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # function to check if database already exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

