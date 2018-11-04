from app import app
from sqlalchemy import create_engine
from db import db


db.init_app(app)
engine = create_engine('sqlite:///data.db')
db.metadata.create_all(engine)

app.run(debug=True)