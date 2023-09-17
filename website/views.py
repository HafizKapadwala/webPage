#url for front end of our website


#in this page we are going to store the roots for our website like -- Home Page

from flask import Blueprint, render_template
#we use render_template to import the templates and use it

#we are going to define that this file is Blueprint for our application, bunch of roots inside

views = Blueprint('views',__name__)

@views.route('/') #this function will run whenever  we go to / route
def home():
    return render_template("home.html",)
    #this will render the home page using the home function