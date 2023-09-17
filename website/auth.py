from flask import Blueprint

#we are going to define that this file is Blueprint for our application, bunch of roots inside
#Login page

auth = Blueprint('auth',__name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup')
def sigup():
    return "<p>signup</p>"