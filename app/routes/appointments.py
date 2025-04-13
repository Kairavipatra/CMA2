from flask import Blueprint, request, jsonify

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

appointments = []

@bp.route('/book', methods=['POST'])
def book():
    data = request.json
    appointments.append(data)
    return jsonify({"status": "Booked", "details": data})
