from flask_app.controllers import login_reg_controller
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
Bcrypt = Bcrypt(app)


ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def new_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """    
        return MySQLConnection(DATABASE).query_db(query, data)
        
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM users WHERE id = %(id)s;
            """
        results = MySQLConnection(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False    
            
    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * from users WHERE email = %(email)s;
        """
        results = MySQLConnection(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("first name must be atleast 2 chars", 'reg')
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("last name must be atleast 2 chars", 'reg')
            is_valid = False
        if len(form_data['email']) < 1:
            flash("valid email required", 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            # if email does not meet regex requirements flash message will appear
            flash("email invalid", 'reg')
            is_valid = False
        else:
            # look up email if its in DB
            data = {
                'email' : form_data['email']    
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("Email already exists", 'reg')
                is_valid = False
        if len(form_data['password']) < 8:
            flash("password must be atleast 8 chars", 'reg')
            is_valid = False
        elif not form_data['password'] == form_data['conf_pass']:
            flash("Passwords must match")
            is_valid = False
        return is_valid