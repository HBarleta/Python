from flask_app import app
# import flask_app init file
from flask_app.controllers import users_controller
#import controller here

# DO NOT FORGET TO PIPENV INSTALL FLASK (server operations), 
# pyMySQL (connects to DB), pipenv install flask-bcrypt (password encryption)

if __name__=="__main__":
    app.run(debug=True)