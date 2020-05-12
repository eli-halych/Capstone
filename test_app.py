import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app import create_app
from controllers import hackathon_api
from models import setup_db, Status, Hackathon

database_path = os.environ['DATABASE_URL']

class DSCTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

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
            self.status_pending = Status(
                name="Pending",
                description="Submitted application"
            )

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_hackathons(self):
        res = self.client().get(
            '/hackathons'
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']

        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathons']), list)

    def test_create_hackathons(self):
        request_body = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending.id
        }
        request_body = json.dumps(request_body)

        res = self.client().post(
            '/hackathons',
            data=request_body
        )
        status_code = res.status_code
        data = json.loads(res.data)
        success = data['success']

        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(type(data['hackathon_id']), int)

    def test_create_one_hackathons(self):
        # checks an existing hackathon
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending.id
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

        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon_id'], requested_id)

    def test_delete_hackathons(self):
        # checks an existing hackathon
        data = {
            "name": "Hackathon_Test",
            "start_time": "2001-01-11T00:00:00",
            "end_time": "2001-01-21T00:00:00",
            "place_name": "Google Campus",
            "status_id": self.status_pending.id
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

        self.assertEqual(status_code, 200)
        self.assertTrue(success)
        self.assertEqual(data['hackathon_id'], requested_id)


if __name__ == "__main__":
    unittest.main()
