from flask_app import app
# import flask_app init file
from flask_app.controllers import dojos_controller
#import controller here

# DO NOT FORGET TO PIPENV INSTALL FLASK (server operations), 
# pyMySQL (connects to DB), flask-bcrypt (encryption for passwords)

if __name__=="__main__":
    app.run(debug=True)