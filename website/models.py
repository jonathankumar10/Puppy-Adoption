# SET UP DB FROM __init__.py File
from website import db

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # # ONE TO MANY RELATIONSHIP (ONE PUPPY CAN HAVE MANY TOYS)
    # toys = db.relationship('Toy', backref = 'puppy', lazy ='dynamic')
    # ONE TO ONE RELATIONSHIP (ONE PUPPY TO ONE OWNER)
    owner = db.relationship('Owner', backref = 'puppy', uselist = False)

    def __init__(self,name):
        self.name = name


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # COLUMN THAT CONNECTS OWNER TO PUPPY
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
