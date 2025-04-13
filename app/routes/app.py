from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def home():
    return render_template('index.html')

@app_bp.route('/Blog')
def blog():
    return render_template('blog.html')

@app_bp.route('/Contact')
def contact():
    return render_template('contact.html')

@app_bp.route('/Dog walking')
def dog_walking():
    return render_template('dog-walking.html')

@app_bp.route('/Healthy Food')
def food():
    return render_template('food.html')

@app_bp.route('/Grooming')
def grooming():
    return render_template('grooming.html')


@app_bp.route('/Services')
def services():
    return render_template('services.html')

@app_bp.route('/Shop')
def shop():
    return render_template('shop.html')

@app_bp.route('/Toys & Treats')
def toys():
    return render_template('toys.html')

@app_bp.route('/Vetrinary')
def vet():
    return render_template('vet.html')
