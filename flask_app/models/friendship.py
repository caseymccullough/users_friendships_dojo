from ..config.mysqlconnection import connectToMySQL

class Friendship:
   def __init__(self, data):
      self.id = data['id']
      self.user_id = data['user_id']
      self.friend_id = data['friend_id']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   def __str__(self):
      return str(self.user_id) + " friends with " + str(self.friend_id)

   @classmethod
   def get_all(cls):
      query = """SELECT  f.id, c1.first_name AS user_first, c1.last_name as user_last, 
			c2.first_name AS friend_first, c2.last_name as friend_last
         FROM friendships AS f
         JOIN users AS c1 ON f.user_id = c1.id
         JOIN users AS c2 ON f.friend_id = c2.id
         ORDER BY f.id;"""
      friendships = []
      results = connectToMySQL('friendships').query_db(query)
      for row in results:
         friendships.append(row)
      print("call to get all(): ")
      print(friendships)
      return friendships

   @classmethod
   def save(cls, data):
      query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, (%(friend_id)s), NOW(), NOW());"
      return connectToMySQL('friendships').query_db(query, data)