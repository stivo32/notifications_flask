from db import db

class NotificationModel(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(80))
    date = db.Column(db.Date())

    def __repr__(self):
        return f"Notification ({self.name}, {self.date})"

    def __init__(self, name, date):
        self.name = name
        self.date = date

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(date=date).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user=user_id).all()
