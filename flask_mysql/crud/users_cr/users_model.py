from mysqlconnection import connectToMySQL
DATABASE = "users_schema"
class Users:
    def __init__(self, data):
        self.user_id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """
        results = connectToMySQL("users_schema").query_db(query)
        # this will query the database and return a list of dictionaries
        all_users = []
        # this list empty list will populate with this for loop
        for user_row in results:
            this_user_instance = cls(user_row)
            all_users.append(this_user_instance)    
        # this for loop takes a user instance
        return all_users
    
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def show_last(cls):
        query = """
            SELECT * FROM users ORDER BY id DESC limit 1;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        this_user = cls(results[0])
        return this_user
        
    @classmethod
    def get_one_user(cls, data):
        query = """
            SELECT * FROM users WHERE users.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def update_user(cls, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s , email = %(email)s
        WHERE users.id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):
        query = """
            DELETE FROM users WHERE users.id = %(id)s
        """
        return connectToMySQL(DATABASE).query_db(query, data)