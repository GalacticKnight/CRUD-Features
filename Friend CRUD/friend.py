from mysqlconnection import connectToMySQL
class Friend:
    DB = "friends"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # the save method will be used when we need to save a new friend to our database
    #CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name,last_name,occupation) VALUES (%(first_name)s,%(last_name)s,%(occupation)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    #READ(only one)
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id = %(id)s;" 
        data = {
            "id":friend_id
        }
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0]) #the reason why its not results[0] is because you want to return an object bck to the server
    #READ(all of them)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends
    #UPDATE
    @classmethod
    def update(cls,data):
        query = """UPDATE friends 
            SET 
            first_name=%(first_name)s,
            last_name=%(last_name)s,
            occupation=%(occupation)s 
            WHERE id = %(id)s;"""
        
        return 
    #DELETE
    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s;"
        data = {"id": friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)

