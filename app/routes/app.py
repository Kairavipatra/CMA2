from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__)

# Define the route for the home page
@app_bp.route('/')
def home():
    return render_template('index.html')

# Define routes for the other pages
@app_bp.route('/blog')
def blog():
    return render_template('blog.html')

@app_bp.route('/contact')
def contact():
    return render_template('contact.html')

@app_bp.route('/dog-walking')
def dog_walking():
    return render_template('dog-walking.html')

@app_bp.route('/food')
def food():
    return render_template('food.html')

@app_bp.route('/grooming')
def grooming():
    return render_template('grooming.html')

@app_bp.route('/payment')
def payment():
    return render_template('payment.html')

@app_bp.route('/services')
def services():
    return render_template('services.html')

@app_bp.route('/shop')
def shop():
    return render_template('shop.html')

@app_bp.route('/toys')
def toys():
    return render_template('toys.html')

@app_bp.route('/vet')
def vet():
    return render_template('vet.html')

