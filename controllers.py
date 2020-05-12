from flask import jsonify, Blueprint, request, json
from werkzeug.exceptions import abort
from models import Hackathon, Item, Status, Category, Workshop

hackathon_api = Blueprint('hackathon_api', __name__)


@hackathon_api.route('/hackathons', methods=['GET'])
def get_hackathons():
    """
        GET /hackathons
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
        POST /hackathons
            it is accessible for authorized DSC members
            it takes up to a full representation of a hackathon

        :return: status code 200 and short descriptions of all hackathons as a list and success status
        {'hackathons': [], 'success': True}
    """

    data = {}
    response = {
        'hackathon_id': None,
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


@hackathon_api.route('/hackathons/<hackathon_id>', methods=['GET'])
def get_one_hackathon(hackathon_id):
    """
        GET /hackathons
            it is accessible for authorized DSC members
            it contains a full representation of a hackathon

        :return: status code 200 and full descriptions of a requested hackathon, success status and
        requested hackathon id
        {'hackathon': {...}, 'success': True, 'hackathon_id': 1}
    """

    data = {}
    response = {
        'hackathon': {},
        'success': False,
        'hackathon_id': None
    }

    if hackathon_id is None:
        abort(400)  # bad request

    try:

        hackathon = Hackathon.query.filter(Hackathon.id == hackathon_id).first()

        if hackathon is None:
            abort(404)  # not found

        response['success'] = True
        response['hackathon_id'] = hackathon.id
        response['hackathon'] = hackathon.full_serialize()
    except:
        abort(422)  # unprocessable

    return jsonify(response)
