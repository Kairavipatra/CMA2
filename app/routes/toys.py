from flask import Blueprint, jsonify

bp = Blueprint('toys', __name__, url_prefix='/toys')

@bp.route('/')
def toy_list():
    return jsonify([
        {"name": "Plush Chew Toy", "price": 300},
        {"name": "Squeaky Bone", "price": 250}
    ])
