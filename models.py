import os
from sqlalchemy import Column, String, create_engine, Integer, DateTime, Boolean, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy_utils import database_exists, create_database

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


class Hackathon(db.Model):
    """
        Main event model connecting workshops, assets, can be approved or rejected by a Developer Students Club's lead
        after being reviewed as an application made by a Developer Students' Club member.

        MANY Hackathon can host MANY Workshop -> associative table Hackathon_Workshop
        MANY Hackathon can have MANY Category -> associative table Hackathon_Category
        MANY Hackathon can have MANY Item -> associative table Hackathon_Item
        ONE Hackathon can have ONE Status
    """

    __tablename__ = 'hackathon'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_time = db.Column(DateTime(timezone=True))
    end_time = db.Column(DateTime(timezone=True))
    place_name = Column(String)

    categories = db.relationship("Hackathon_Category", cascade="all,delete", backref="category")
    workshops = db.relationship("Hackathon_Workshop", cascade="all,delete", backref="workshop")
    # TODO items = # fk
    # TODO status = # fk

    def short_serialize(self):
        """
        short_serialize()
            short form representation of the Hackathon model
        """

        return {
            'id': self.id,
            'name': self.name,
            'time': self.time,
            'place': self.place
        }

    def full_serialize(self):
        """
            full_serialize()
                full form representation of the Hackathon model
        """
        return {
            'id': self.id,
            'name': self.name,
            'time': self.time,
            'place': self.place,
            # TODO get childern's names
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.full_serialize())


class Workshop(db.Model):
    """
        Workshop events run within a hackathon (many to many relationship)
    """

    __tablename__ = 'workshop'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    speaker_name = Column(String)
    participants = Column(Integer)
    duration = Column(String)
    speaker_phone = Column(String)

    hackathons = db.relationship("Hackathon_Workshop", cascade="all,delete", backref="hackathon")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'speaker_name': self.speaker_name,
            'speaker_phone': self.speaker_phone,
        }

    def __repr__(self):
        return json.dumps(self.serialize())


class Category(db.Model):
    """
        Categories a hackathon belongs to (many to many relationship)
    """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    hackathons = db.relationship("Hackathon_Category", cascade="all,delete", backref="hackathon")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def __repr__(self):
        return json.dumps(self.serialize())


class Item(db.Model):
    """
        Needed or available assets for a hackathon (many to many relationship)
    """

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # TODO hackathons = # fk with flags have/need

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def __repr__(self):
        return json.dumps(self.serialize())


class Status(db.Model):
    """
        3 types of hackathon statuses: approved, rejected, pending (one to one relationship)
    """

    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # TODO hackathon = # fk

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def __repr__(self):
        return json.dumps(self.serialize())


class Hackathon_Workshop(db.Model):
    """
        Serves as a connection (assignation) between a workshop and a hackathon.
    """

    __tablename__ = 'hackathon_workshop'

    id = db.Column(Integer, primary_key=True)
    hackathon_id = Column(Integer, ForeignKey('hackathon.id'))
    workshop_id = Column(Integer, ForeignKey('workshop.id'))
    event_description = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'hackathon_id': self.hackathon_id,
            'workshop_id': self.workshop_id,
            "event_description": self.event_description
        }

    def __repr__(self):
        return json.dumps(self.serialize())


class Hackathon_Category(db.Model):
    """
        Serves as a connection (assignation) between a category and a hackathon.
    """

    __tablename__ = 'hackathon_category'

    id = db.Column(Integer, primary_key=True)
    hackathon_id = Column(Integer, ForeignKey('hackathon.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    def serialize(self):
        return {
            'id': self.id,
            'hackathon_id': self.hackathon_id,
            'category_id': self.category_id,
        }

    def __repr__(self):
        return json.dumps(self.serialize())


def setup_db(app, database_path=database_path):
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
        contains 2 options to create tables in the database, works depending on your system
    """

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    # option one to create
    db.drop_all()
    db.create_all()

    # # option 2 to create (depends on the machine)
    # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    # if not database_exists(engine.url):
    #     create_database(engine.url)
