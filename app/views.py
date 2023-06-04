from flask import Blueprint
from sqlalchemy.orm import Session

from app import db
from app.models import Employee, Position, Division, Job
from sqlalchemy.orm import sessionmaker

bp = Blueprint('bp', __name__)


@bp.route('/', methods=['GET'])
def index():
    return '1'
