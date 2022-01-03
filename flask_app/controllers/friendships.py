from flask_app import app
from flask import redirect, render_template, request
from ..models.user import User
from ..models.friendship import Friendship

@app.route('/friendships')
def friendships():
   return render_template('/friendships.html', all_users = User.get_all(), all_friendships = Friendship.get_all())

@app.route('/create/friendship', methods=['POST'])
def create_friendship():
   data = {
      "user_id" : request.form['user_id'],
      "friend_id" : request.form['friend_id']
   }
   friendship_id = Friendship.save(data)
   return redirect('/friendships')