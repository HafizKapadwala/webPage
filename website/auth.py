from flask import Blueprint,render_template,request,flash

#we are going to define that this file is Blueprint for our application, bunch of roots inside
#Login page

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form #we can access all the form that came through the website
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup',methods=['GET','POST'])
def sigup():
    if request.method == 'POST':
        email = request.form.get('email') #to get the email from the post request
        firstName = request.form.get('firstName')
        pass1 = request.form.get('password1')
        pass2 = request.form.get('password2')

        if len(email) < 4:
            flash("email should be more than 4 characters",category='error')
        elif len(firstName) < 2:
            flash("email should be more than 4 characters", category='error')
        elif pass1 != pass2:
            flash("email should be more than 4 characters", category='error')
        elif len(pass1) < 7:
            flash("email should be more than 4 characters", category='error')
        else:
            flash("Account Created",category="success")

    return render_template("sender.html")