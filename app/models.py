from app import db

class DriverModel(db.Model):
    __tablename__ = "driver"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    selected_rider = db.Column(db.Integer)
    available = db.Column(db.Boolean)
    amountMoney = db.Column(db.Float)
    ratings = db.relationship('RatingModel', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Driver {}>'.format(self.name)

class RiderModel(db.Model):
    __tablename__ = "rider"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index = True)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    groupHost = db.Column(db.String(64))
    destination = db.Column(db.String(128))
    selected_driver = db.Column(db.Integer)
    outstandingBalance = db.Column(db.Float)
    
    def __repr__(self):
        return '<Rider {}>'.format(self.name)



class AdminModel(db.Model):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Admin {}>'.format(self.name)


    
class RatingModel (db.Model):

    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Rating {}>'.format(self.name)    
