from flask import Blueprint, request, jsonify

# Define the blueprint
foster_care_bp = Blueprint('foster_care', __name__, url_prefix='/foster-care')

# Temporary in-memory list to store foster applications
foster_requests = []

# Route to handle foster applications
@foster_care_bp.route('/apply', methods=['POST'])
def apply_foster():
    data = request.get_json()

    # Basic input validation
    required_fields = ['name', 'email', 'phone', 'pet_preference', 'address']
    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({
            "status": "Failed",
            "message": f"Missing required fields: {', '.join(missing)}"
        }), 400

    foster_requests.append(data)
    return jsonify({
        "status": "Success",
        "message": "Foster application received!",
        "application": data
    }), 201

# Route to list available foster homes
@foster_care_bp.route('/list', methods=['GET'])
def list_fosters():
    available_fosters = [
        {
            "name": "Airoli Pet Foster Home",
            "address": "Plot 12, Sector 8A, Airoli, Navi Mumbai",
            "contact": "9876543210"
        },
        {
            "name": "Paw Haven",
            "address": "Sector 4, Airoli, Navi Mumbai",
            "contact": "9123456789"
        },
        {
            "name": "Furry Friends Shelter",
            "address": "Near Mindspace, Airoli, Navi Mumbai",
            "contact": "9812345678"
        }
    ]

    return jsonify({
        "status": "Success",
        "available_fosters_in_airoli": available_fosters
    }), 200
