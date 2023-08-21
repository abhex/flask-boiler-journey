from flask import Blueprint

bp = Blueprint('users', __name__)

from app.users import routes
# from app.users.model import User # For Migrations
