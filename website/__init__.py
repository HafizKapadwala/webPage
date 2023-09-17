#This init.py is the python file that is going to make -- website --> as python package

#we can import this folder called website so that whenever we run the website this python file will run automatically.

from flask import Flask


#initializing the flask app
def create_app():
    app = Flask(__name__)
    #this is going to encrypt cookies and session data regarding our website
    app.config['SECRET_KEY'] = 'team_43_CMPT370'
    #never share this secret key with anybody.
    return app