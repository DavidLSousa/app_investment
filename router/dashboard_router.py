from flask import (
    Blueprint
)
from src.controller import dashboard_controller

dashboard_bp = Blueprint('dashboard', __name__)
