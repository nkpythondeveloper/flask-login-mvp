from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder="/app/templates")

from . import auth