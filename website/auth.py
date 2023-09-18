from flask import Blueprint,render_template,request 

#we are going to define that this file is Blueprint for our application, bunch of roots inside
#Login page

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup',methods=['GET','POST'])
def sigup():
    return render_template("sender.html")