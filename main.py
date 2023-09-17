# Creating a web App - Backend,Flask and Python(Practice for the project)


#This the main.py file that we will run when we want to start a webserver


from website import create_app

app = create_app()

#this will create a webserver only it will run when this file is running, not if it is called from any other py files
if __name__ == '__main__':
    app.run(debug=True)#debug=true means that whenever we make a change in our webserver it will automatically run that
    # first it will run, but we will not be able to see anything cause we dont have the home page or root for our website


