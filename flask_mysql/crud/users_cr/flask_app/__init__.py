from flask import Flask
app = Flask(__name__)
app.secret_key = "Ninjas don't lie"
# secret key for session
DATABASE = "users_schema" 
# global variable for schema