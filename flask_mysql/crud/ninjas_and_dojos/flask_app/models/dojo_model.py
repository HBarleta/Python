from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for one_row in results:
            this_dojo_instance = cls(one_row)
            all_dojos.append(this_dojo_instance)
        return all_dojos
    
    @classmethod
    def get_one(cls, data):
        query = """
            SELECT name FROM dojos WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]

    @classmethod
    def add_dojo(cls,data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s)
        """
        return connectToMySQL(DATABASE).query_db(query, data)