from flask import jsonify, Blueprint, request, json
from werkzeug.exceptions import abort
from models import Hackathon, Item, Status, Category, Workshop

hackathon_api = Blueprint('hackathon_api', __name__)


@hackathon_api.route('/hackathons', methods=['GET'])
def get_hackathons():
    """
        GET /drinks
            it is accessible for authorized DSC members
            it contains only the short data representation

        :return: status code 200 and short descriptions of all hackathons as a list and success status
        {'hackathons': [], 'success': True}
    """

    response = {
        'hackathons': [],
        'success': False
    }

    try:
        hackathons = Hackathon.query.all()
        serialized_short = [hackathon.short_serialize() for hackathon in hackathons]
        response['hackathons'] = serialized_short
        response['success'] = True
    except:
        abort(404)  # not found

    return jsonify(response)


@hackathon_api.route('/hackathons', methods=['POST'])
def create_hackathon():
    """
        POST /drinks
            it is accessible for authorized DSC members
            it takes up to a full representation of a hackathon

        :return: status code 200 and short descriptions of all hackathons as a list and success status
        {'hackathons': [], 'success': True}
    """

    data = {}
    response = {
        'hackathon_id': [],
        'success': False
    }

    try:
        data = json.loads(request.data)
    except:
        abort(400)  # bad request

    try:

        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()

        response['success'] = True
        response['hackathon_id'] = hackathon.id
    except:
        abort(422)  # unprocessable

    return jsonify(response)
