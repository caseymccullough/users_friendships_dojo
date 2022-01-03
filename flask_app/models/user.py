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
   def get_by_id(cls, data):
      query = "SELECT * FROM users WHERE users.id = %(id)s;"
      friend_query = "SELECT friendships.created_at, users.id, users.first_name, users.last_name FROM friendships.friendships LEFT JOIN users ON friendships.friend_id = users.id WHERE user_id = %(id)s;"
      results = connectToMySQL('friendships').query_db(query,data)
      friends = connectToMySQL('friendships').query_db(friend_query, data)
      user = cls(results[0])
      user.friendships = friends

      print ("user in get_by_id", results[0])
      print("friends in user.friendships", user.friendships)
      # append all friendship objects to the instances favorites list.
      #for row in results:
         # if there are no favorites
            # if row['friendship.id'] == None:
            #     break
            # print(row)
            # common column names come back with specific tables attached
            # data = {
            #     "id": row['books.id'],
            #     "title": row['title'],
            #     "num_of_pages": row['num_of_pages'],
            #     "created_at": row['books.created_at'],
            #     "updated_at": row['books.updated_at']
            # }
            
            # user.friendships.append(book.Book(data))
      return user

   @classmethod
   def save(cls, data):
      query = "INSERT INTO users (first_name, last_name, updated_at) VALUES (%(first_name)s, (%(last_name)s), NOW());"
      return connectToMySQL('friendships').query_db(query, data)

   @classmethod
   def delete(cls, data):
      query = "DELETE FROM users WHERE id = %(id)s;" # cascades so friendships will be removed as well
      results = connectToMySQL('users').query_db(query, data)
      return results