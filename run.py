from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    from models.user import UserModel
    from models.notification import NotificationModel
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)