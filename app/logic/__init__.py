from flask import Blueprint

logic_bp = Blueprint("logic", __name__, template_folder="/app/templates")

from . import logic