from flask import Blueprint, request, jsonify

bp = Blueprint('dog_walking', __name__, url_prefix='/dog-walking')

walk_schedule = []

@bp.route('/schedule', methods=['POST'])
def schedule_walk():
    data = request.json
    walk_schedule.append(data)
    return jsonify({"status": "Scheduled", "data": data})
