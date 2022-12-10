from flask import Flask
app = Flask(__name__)
app.secret_key = "Ninjas don't lie"
DATABASE = "users_schema"