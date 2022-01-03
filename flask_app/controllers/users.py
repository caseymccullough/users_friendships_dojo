from flask_app import app
from flask import redirect, render_template, request
from ..models.user import User
from ..models.friendship import Friendship

@app.route('/')
def index():
   return redirect('/users')

@app.route('/users')
def users():
   return render_template('/users.html', all_users = User.get_all())

@app.route('/users/<int:id>')
def show_user(id):
   data = {
      "id" : id
   }
   print("data in route:", data)
   user = User.get_by_id(data)
   print("user in route:", user)
   return render_template('user.html', user = user)

@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):
   data = {
      "id" : id
   }
   print("data in route:", data)
   user = User.delete(data)
   print("user in route:", user)
   return redirect('/users')

@app.route('/create/user', methods=['POST'])
def create_user():
   data = {
      "first_name" : request.form['first_name'],
      "last_name" : request.form['last_name']
   }
   user_id = User.save(data)
   return redirect('/')


