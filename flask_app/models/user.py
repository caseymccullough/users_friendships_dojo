from ..config.mysqlconnection import connectToMySQL

class User:
   def __init__(self, data):
      self.id = data['id']
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   def __str__(self):
      return "" + self.first_name + " " + self.last_name

   @classmethod
   def get_all(cls):
      query = "SELECT * FROM users;"
      users = []
      results = connectToMySQL('friendships').query_db(query)
      for row in results:
         users.append(cls(row))
      print("call to get all(): ")
      print(users)
      return users

   @classmethod
   def save(cls, data):
      query = "INSERT INTO users (first_name, last_name, updated_at) VALUES (%(first_name)s, (%(last_name)s), NOW());"
      return connectToMySQL('friendships').query_db(query, data)