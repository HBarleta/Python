from flask_app.config.mysqlconnection import connectToMySQL
# imports mysqlconnection file for DB queries
from flask_app import app
from flask_app import DATABASE
#imports global variable name for DB schema
from flask import flash
# import flash for validation
import re
# imports regex library for validation
# DO NOT FORGET TO UPDATE FILE NAME TO REFLECT PROJECT USING PROPER 
# NAMING CONVENTION

# template for bcrypt 
 

ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$")
# regex for alphanumeric inputs in validator
# for other regex check w3 schools for other regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email regex for validator


# example of init class
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
# this will utilize a password encryption using bcrypt
# example for login page





# insert template
@classmethod
def create(cls,data):
    query = """
    INSERT INTO USERS (first_name, last_name, email, password)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
        return cls(results[0])
    else:
        return False
    
    
    # template for getting a targeting a single ID
@classmethod
def get_by_id(cls,data):
    query = """
        SELECT * FROM (name of database) WHERE id = %(id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query, data)
    if results:
        return cls(results[0])
    return False

@classmethod
def get_by_email(cls,data):
    query = """
        SELECT * FROM (name of database) WHERE email = %(email)s;
    """
    results = connectToMySQL(DATABASE).query_db(query, data)
    if results:
        return cls(results[0])  
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


# general validator static method
@staticmethod
def validator(potential):
    is_valid = True
    # validator will check if forms are filled out according to these rules below
    
    # this will check if anything was inputted into the form 
    # and reject if left blank
    if len(potential['name']) < 1:
        # this rule will check form['name'] for any input / character leng
        is_valid = False
        flash("tell them what is wrong such as length or requirement in the form", "name")
        # second argument "name" refers to the name of the field and is the category filter
    elif not ALPHANUMERIC.match(potential['name']):
        # this will check if the input in name field is alphanumeric
        is_valid = False
        flash("name cannot contain special characters")
        # this will flash a message if special characters are used
    # check integer values
    
    if len(potential['int']) < 1:
        # this will check for an integer was inputted
        is_valid = False
        flash("tell them what is wrong such as length or requirement in the form")   
        # if an integer was inputted this will 
        # check if it is a positive number
    elif int(potential['int']) < 0:
        is_valid = False    
        flash("must be positive number") 
    
    # check for validation of checkbox
    if "key in form for check box" not in potential['checkboxname']:
        is_valid = False
        flash("this check box was not checked")
        # this works for radio buttons too
    
    
    
    return is_valid
    # if input passes all validators this will return true
    # else it will reject inputs

