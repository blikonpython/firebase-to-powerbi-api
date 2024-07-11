from flask import Blueprint, jsonify
from .controllers import DataController

main = Blueprint('main', __name__)
controller = DataController()

@main.route('/api/getAllVisits', methods=['GET'])
def get_all_visits():
    data = controller.get_all_visits()
    return jsonify(data), 200
