from ..config.mysqlconnection import connectToMySQL

class Friendship:
   def __init__(self, data):
      self.id = data['id']
      self.user_id = data['user_id']
      self.friend_id = data['friend_id']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   def __str__(self):
      return "" + self.user_id + " friends with " + self.friend_id

   @classmethod
   def get_all(cls):
      query = "SELECT * FROM friendships;"
      friendships = []
      results = connectToMySQL('friendships').query_db(query)
      for row in results:
         friendships.append(cls(row))
      print("call to get all(): ")
      print(friendships)
      return friendships

   @classmethod
   def save(cls, data):
      query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, (%(friend_id)s), NOW(), NOW());"
      return connectToMySQL('friendships').query_db(query, data)