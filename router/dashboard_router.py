from flask import (
    Blueprint,
    request
)
from src.controller import dashboard_controller

dashboard_bp = Blueprint('dashboard', __name__)
