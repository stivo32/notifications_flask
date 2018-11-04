from db import db

class NotificationModel(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(160))
    date = db.Column(db.Date())

    def __repr__(self):
        return f"Notification ({self.message}, {self.date})"

    def __init__(self, message, date):
        self.message = message
        self.date = date

    def jsonify(self):
        return {"message": self.message,
                "date": self.date}

    @classmethod
    def find_by_message(cls, message):
        return cls.query.filter_by(name=message).first()

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(date=date).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user=user_id).first()
