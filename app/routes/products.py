from flask import Blueprint, jsonify

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/')
def list_products():
    products = [
        {"name": "Premium Dog Food", "price": 500},
        {"name": "Catnip Ball", "price": 200},
        {"name": "Salmon Treats", "price": 150}
    ]
    return jsonify(products)
