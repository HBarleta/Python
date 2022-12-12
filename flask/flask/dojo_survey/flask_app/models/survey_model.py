from flask import flash
from flask_app.controllers import survey_controller
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
import re
ALPHA = re.compile(r"^[a-zA-Z]+$")

class Survey:
    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language'] 
        self.comment = data['comment'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_survey(cls, data):
            query = """
                INSERT INTO dojos (name, location, language, comment)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)
            """
            return connectToMySQL(DATABASE).query_db(query, data) 
        
    @classmethod
    def get_last(cls):
        query = """
        SELECT * FROM dojos ORDER BY id DESC LIMIT 1;
        """
        
        results = connectToMySQL(DATABASE).query_db(query)
        dojo_instance = cls(results[0])
        if results:
            return dojo_instance
        else:
            return False
        
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 2:
            flash("name must be atleast 2 chars", 'reg')
            is_valid = False
        elif not ALPHA.match(form_data['name']):
            flash("Cannot use special characters or numbers", 'reg')
            is_valid = False
        return is_valid