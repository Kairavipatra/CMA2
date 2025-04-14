#from flask import Blueprint, request, redirect, url_for, render_template_string

#auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#users = {}

#@auth_bp.route('/signup', methods=['GET', 'POST'])
#def signup():
    #if request.method == 'POST':
        #username = request.form['username']
       # password = request.form['password']
      #  users[username] = password
        # Redirect to home after successful signup
     #   return redirect(url_for('app.home'))
    #return '''
      #  <form method="post">
     #       Username: <input type="text" name="username" required>
    #        Password: <input type="password" name="password" required>
   #         <button type="submit">Sign Up</button>
  #      </form>
 #   '''

#@auth_bp.route('/login', methods=['GET', 'POST'])
#def login():
   # if request.method == 'POST':
       # username = request.form['username']
       # password = request.form['password']
      #  if users.get(username) == password:
            # Redirect to home after successful login
     #       return redirect(url_for('app.home'))
    #    return "Invalid credentials."
   # return '''
       # <form method="post">
      #      Username: <input type="text" name="username" required>
     #       Password: <input type="password" name="password" required>
    #        <button type="submit">Login</button>
   #     </form>
  #  '''
from flask import Blueprint, request, redirect, url_for, render_template_string
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Check if username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            return "Username already exists.", 400  # Return a 400 Bad Request error if username exists
        
        # Create a new user with hashed password
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))  # Redirect to login page after successful signup

    return '''
        <form method="post">
            Username: <input type="text" name="username" required>
            Password: <input type="password" name="password" required>
            <button type="submit">Sign Up</button>
        </form>
    '''


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # Log the user in
            return redirect(url_for('admin.index'))  # Redirect to Admin Panel

        return "Invalid credentials.", 401  # Unauthorized if login fails

    return '''
        <form method="post">
            Username: <input type="text" name="username" required>
            Password: <input type="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    '''


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
