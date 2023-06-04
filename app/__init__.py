from flask import Flask
from flask_migrate import Migrate


from app.db import db
from app.views import bp
from templates.config import Config

from app.models import Employee, Position, Division, Job

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
