#This init.py is the python file that is going to make -- website --> as python package

#we can import this folder called website so that whenever we run the website this python file will run automatically.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
#this will initialize our database
DB_NAME = "database.db"
#this is creating our database name


#initializing the flask app
def create_app():
    app = Flask(__name__)
    #this is going to encrypt cookies and session data regarding our website
    app.config['SECRET_KEY'] = 'team_43_CMPT370'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #this just tell our flask app where our database is located
    #never share this secret key with anybody.
    db.init_app(app)
    #we are just telling our database where the app is

    #if we are going to store something in our database --> then we have to show how the object looks like
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/') #That means we have to go through / we can also add prefix if we want to

    from .models import User,Note
    #we do this to make sure that classes are created in database
    create_database(app)
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("CreatedDatabase")
        #this will create a database if it is not created.
