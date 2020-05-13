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
        GET /hackathons/<hackathon_id>
            it is accessible for authorized DSC members
            it contains a full representation of a hackathon

        :return: status code 200 and full descriptions of a requested hackathon, success status and
        requested hackathon id
        {'hackathon': {...}, 'success': True, 'hackathon_id': 1}
    """

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


@hackathon_api.route('/hackathons/<hackathon_id>', methods=['DELETE'])
def delete_hackathon(hackathon_id):
    """
        DELETE /hackathons/<hackathon_id>
            removes requested hackathon frm the database

        :return: status code 200, success status and removed hackathon's id
        {'success': True, 'hackathon_id': 1}
    """

    response = {
        'success': False,
        'hackathon_id': None
    }

    if hackathon_id is None:
        abort(400)  # bad request

    try:

        hackathon = Hackathon.query.filter(Hackathon.id == hackathon_id).first()

        if hackathon is None:
            abort(404)  # not found

        hackathon.delete()

        response['success'] = True
        response['hackathon_id'] = hackathon.id
    except:
        abort(422)  # unprocessable

    return jsonify(response)


@hackathon_api.route('/hackathons/<hackathon_id>', methods=['PATCH'])
def approve_hackathon(hackathon_id):
    """
        PATCH /hackathons/<hackathon_id>
            changes hackathon's status

        :return: status code 200, success status and hackathon's ID,  the new status and updated hackathon
        {'success': True, 'hackathon_id': 1, 'status': 'Approved, 'hackathon': {...}}
    """

    data = {}
    response = {
        'success': False,
        'hackathon_id': None,
        'status': None,
        'hackathon': {}
    }

    if hackathon_id is None:
        abort(400)  # bad request

    try:
        data = json.loads(request.data)
    except:
        abort(400)  # bad request

    try:
        status = Status.query.filter(Status.id == data['status_id']).first()
        hackathon = Hackathon.query.filter(Hackathon.id == hackathon_id).first()

        if hackathon is None:
            abort(404)  # not found

        hackathon.status = status

        hackathon.update()

        response['success'] = True
        response['hackathon_id'] = hackathon.id
        response['status'] = status.name
        response['hackathon'] = hackathon.full_serialize()
    except:
        abort(422)  # unprocessable

    return jsonify(response)


@hackathon_api.route('/hackathons/<hackathon_id>', methods=['PUT'])
def edit_hackathon(hackathon_id):
    """
        PUT /hackathons/<hackathon_id>
            updates all hackathon's details except those belonging to relationships
            # TODO update relationships

        :return: status code 200, success status, hackathon's ID and the updated hackathon
        {'success': True, 'hackathon_id': 1, 'hackathon': {...}}
    """

    data = {}
    response = {
        'success': False,
        'hackathon_id': None,
        'hackathon': {}
    }

    if hackathon_id is None:
        abort(404)  # not found

    try:
        data = json.loads(request.data)
    except:
        abort(400)  # bad request

    try:
        hackathon = Hackathon.query.filter(Hackathon.id == hackathon_id).first()

        hackathon.name = data['name']
        hackathon.start_time = data['start_time']
        hackathon.end_time = data['end_time']
        hackathon.place_name = data['place_name']

        hackathon.update()

        if hackathon is None:
            abort(404)  # not found

        hackathon.update()

        response['success'] = True
        response['hackathon_id'] = hackathon.id
        response['hackathon'] = hackathon.full_serialize()
    except:
        abort(422)  # unprocessable

    return jsonify(response)


@hackathon_api.errorhandler(422)
def unprocessable(error):
    """"
        Unable to process an understood request
    """
    return jsonify({
        "success": False,
        "error": 422,
        "message": str(error)
    }), 422


@hackathon_api.errorhandler(404)
def not_found(error):
    """"
        Requested element not found
    """
    return jsonify({
        "success": False,
        "error": 404,
        "message": str(error)
    }), 404


@hackathon_api.errorhandler(400)
def bad_request(error):
    """"
        Bad request.
    """
    return jsonify({
        "success": False,
        "error": 400,
        "message": str(error)
    }), 400


@hackathon_api.errorhandler(401)
def not_authorized(error):
    """"
        Authorized access.
    """
    return jsonify({
        "success": False,
        "error": 401,
        "message": str(error)
    }), 401


@hackathon_api.errorhandler(403)
def forbidden(error):
    """"
        Forbidden actions.
    """
    return jsonify({
        "success": False,
        "error": 403,
        "message": str(error)
    }), 403