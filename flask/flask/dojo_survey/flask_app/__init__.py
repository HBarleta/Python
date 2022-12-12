from flask import Flask
app = Flask(__name__)
app.secret_key = "There are no secrets in the dojo"
DATABASE = "dojo_survey_schema"