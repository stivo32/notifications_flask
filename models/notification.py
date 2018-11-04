from db import db


class NotificationModel(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(160))
    date = db.Column(db.Date())

    def __repr__(self):
        return "Notification ({message}, {date})".format(message=self.message, date=self.date)

    def __init__(self, message, date):
        self.message = message
        self.date = date

    def jsonify(self):
        return {"message": self.message,
                "date": self.date}

    @classmethod
    def find_by_message_and_user_id(cls, message):
        return cls.query.filter_by(name=message).first()

    @classmethod
    def find_by_date_and_user_id(cls, date):
        return cls.query.filter_by(date=date).first()

