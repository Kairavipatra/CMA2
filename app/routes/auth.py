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

from flask import Blueprint, request, redirect, url_for, render_template_string, flash
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
            flash('Username already exists.', 'error')  # Flash error message
            return redirect(url_for('auth.signup'))  # Stay on signup page if username exists
        
        # Create a new user with hashed password
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Sign-up successful! Please log in.', 'success')  # Flash success message
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

            # Redirect to the page user wanted to visit (next parameter), or fallback to home page
            next_page = request.args.get('next')
            return redirect(next_page or url_for('app.home'))  # Adjust to your home route

        flash('Invalid credentials.', 'error')  # Flash error message
        return redirect(url_for('auth.login'))  # Stay on login page if credentials are incorrect

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
    flash('You have been logged out.', 'info')  # Flash logout message
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
