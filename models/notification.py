from db import db


class NotificationModel(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(160))
    date = db.Column(db.DateTime())

    def __repr__(self):
        return "Notification ({message}, {date})".format(message=self.message, date=self.date)

    def __init__(self, message, user_id, date):
        self.message = message
        self.date = date
        self.user_id = user_id

    def jsonify(self):
        return {
                "message": self.message,
                "date": self.date.strftime("%A, %d. %B %Y %I:%M%p")
            }

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_message_and_user_id(cls, message, user_id):
        return cls.query.filter_by(user_id=user_id).filter_by(message=message).first()

    @classmethod
    def find_by_date_and_user_id(cls, date, user_id):
        return cls.query.filter_by(user_id=user_id).filter_by(date=date).first()

