from flask import Flask
app = Flask(__name__)
app.secret_key = "Don't lie my ninja"
DATABASE = "login_and_register_schema"