from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def home():
    return render_template('index.html')

@app_bp.route('/blog')  # Changed to lowercase and no spaces
def blog():
    return render_template('blog.html')

@app_bp.route('/contact')  # Changed to lowercase and no spaces
def contact():
    return render_template('contact.html')

@app_bp.route('/dog-walking')  # Changed to hyphen and lowercase
def dog_walking():
    return render_template('dog-walking.html')

@app_bp.route('/healthy-food')  # Changed to lowercase and hyphen
def food():
    return render_template('food.html')

@app_bp.route('/grooming')  # Changed to lowercase
def grooming():
    return render_template('grooming.html')

@app_bp.route('/services')  # Changed to lowercase
def services():
    return render_template('services.html')

@app_bp.route('/shop')  # Changed to lowercase
def shop():
    return render_template('shop.html')

@app_bp.route('/toys-treats')  # Changed to lowercase and hyphen
def toys():
    return render_template('toys.html')

@app_bp.route('/veterinary')  # Changed to lowercase and fixed typo
def vet():
    return render_template('vet.html')
