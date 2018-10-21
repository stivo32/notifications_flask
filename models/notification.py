from db import db

class NotificationModel(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel', lazy='dynamic')
    name = db.Column(db.String(80))
    date = db.Column(db.Date())

    def __init__(self):
