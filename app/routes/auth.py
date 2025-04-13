from flask import Blueprint, request, redirect, url_for, render_template_string

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

users = {}

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return "Signup successful!"
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
        if users.get(username) == password:
            return "Login successful!"
        return "Invalid credentials."
    return '''
        <form method="post">
            Username: <input type="text" name="username" required>
            Password: <input type="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    '''
