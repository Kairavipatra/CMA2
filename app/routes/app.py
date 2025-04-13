from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def home():
     return render_template('index.html')
