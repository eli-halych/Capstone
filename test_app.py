import json
import os
import unittest

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app import create_app
from controllers import hackathon_api
from models import setup_db, Status, Hackathon
from utils import get_lead_token, get_member_token

database_path = os.environ['DATABASE_URL']


class DSCTestCase(unittest.TestCase):
    """
        Contains 6 tests each one checking permissions for member/lead/public users.
        Requires a fresh JWT token for both users.
        # TODO switch to pytest
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.app.register_blueprint(hackathon_api)

            # create all tables
            engine = create_engine(self.app.config['SQLALCHEMY_DATABASE_URI'])
            if not database_exists(engine.url):
                create_database(engine.url)

            # test status
            status_pending = Status(
                name="Pending",
                description="Submitted application"
            )
            status_approved = Status(
                name="Approved",
                description="Hackathon approved"
            )

            status_pending.insert()
            status_approved.insert()

            self.status_pending_id = status_pending.id
            self.status_approved_id = status_approved.id

            self.lead_headers = {"Authorization": f"Bearer {get_lead_token()}"}
            self.member_headers = {"Authorization": f"Bearer {get_member_token()}"}

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_hackathons_lead(self):
        # lead test
        res = self.client().get(
            '/hackathons',
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathons']), list)

    def test_get_hackathons_member(self):
        # member test
        res = self.client().get(
            '/hackathons',
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathons']), list)

    def test_get_hackathons_public(self):
        # public test
        res = self.client().get(
            '/hackathons'
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)

    def test_create_hackathons_lead(self):
        # lead test
        request_body = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_body = json.dumps(request_body)
        res = self.client().post(
            '/hackathons',
            data=request_body,
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathon_id']), int)

    def test_create_hackathons_member(self):
        # member test
        request_body = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_body = json.dumps(request_body)
        res = self.client().post(
            '/hackathons',
            data=request_body,
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathon_id']), int)

    def test_create_hackathons_public(self):
        # public test
        request_body = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_body = json.dumps(request_body)
        res = self.client().post(
            '/hackathons',
            data=request_body
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)

    def test_create_one_hackathons_lead(self):
        # lead test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().get(
            f'/hackathons/{requested_id}',
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon_id'], requested_id)

    def test_create_one_hackathons_member(self):
        # member test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().get(
            f'/hackathons/{requested_id}',
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon_id'], requested_id)

    def test_create_one_hackathons_public(self):
        # public test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().get(
            f'/hackathons/{requested_id}'
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)

    def test_delete_hackathons_lead(self):
        # lead test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().delete(
            f'/hackathons/{requested_id}',
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon_id'], requested_id)

    def test_delete_hackathons_member(self):
        # member test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().delete(
            f'/hackathons/{requested_id}',
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 403)
        self.assertTrue(not success)

    def test_delete_hackathons_public(self):
        # public test
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            place_name=data['place_name'],
            status_id=data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().delete(
            f'/hackathons/{requested_id}'
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)

    def test_partially_update_hackathons_lead(self):
        # lead test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_data = {
            'status': "Approved",
            'status_id': self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().patch(
            f'/hackathons/{requested_id}',
            data=request_data_json,
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon']['status_id'], request_data['status_id'])
        self.assertEqual(data['hackathon_id'], requested_id)

    def test_partially_update_hackathons_member(self):
        # member test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_data = {
            'status': "Approved",
            'status_id': self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().patch(
            f'/hackathons/{requested_id}',
            data=request_data_json,
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 403)
        self.assertTrue(not success)

    def test_partially_update_hackathons_public(self):
        # public test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        request_data = {
            'status': "Approved",
            'status_id': self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        requested_id = hackathon.id
        res = self.client().patch(
            f'/hackathons/{requested_id}',
            data=request_data_json
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        hackathon.delete()
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)

    def test_edit_hackathon_lead(self):
        # lead test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        request_id = hackathon.id
        request_data = {
            "name": "Hackathon_Test_Changed",
            "start_time": "2001-01-12T00:00:00",
            "end_time": "2001-01-22T00:00:00",
            "place_name": "Google Campus Changed",
            "status_id": self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        res = self.client().put(
            f'/hackathons/{request_id}',
            data=request_data_json,
            headers=self.lead_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        received_hackathon = data['hackathon']
        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(received_hackathon['name'], request_data['name'])
        self.assertEqual(received_hackathon['place_name'], request_data['place_name'])

    def test_edit_hackathon_member(self):
        # member test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        request_id = hackathon.id
        request_data = {
            "name": "Hackathon_Test_Changed",
            "start_time": "2001-01-12T00:00:00",
            "end_time": "2001-01-22T00:00:00",
            "place_name": "Google Campus Changed",
            "status_id": self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        res = self.client().put(
            f'/hackathons/{request_id}',
            data=request_data_json,
            headers=self.member_headers
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 403)
        self.assertTrue(not success)

    def test_edit_hackathon_public(self):
        # public test
        hackathon_data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending_id
        }
        hackathon = Hackathon(
            name=hackathon_data['name'],
            start_time=hackathon_data['start_time'],
            end_time=hackathon_data['end_time'],
            place_name=hackathon_data['place_name'],
            status_id=hackathon_data['status_id'],
        )
        hackathon.insert()
        request_id = hackathon.id
        request_data = {
            "name": "Hackathon_Test_Changed",
            "start_time": "2001-01-12T00:00:00",
            "end_time": "2001-01-22T00:00:00",
            "place_name": "Google Campus Changed",
            "status_id": self.status_approved_id
        }
        request_data_json = json.dumps(request_data)
        res = self.client().put(
            f'/hackathons/{request_id}',
            data=request_data_json
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']
        self.assertEqual(status_code, 401)
        self.assertTrue(not success)


if __name__ == "__main__":
    unittest.main()
