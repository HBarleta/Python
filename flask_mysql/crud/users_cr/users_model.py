from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
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
        
        all_users = []
        
        for user_row in results:
            this_user_instance = cls(user_row)
            all_users.append(this_user_instance)
        return all_users
    
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (id, first_name, last_name, email)
            VALUES (%(id)s,%(first_name)s,%(last_name)s,%(email)s);
        """
        return connectToMySQL("users_schema").query_db(query, data)