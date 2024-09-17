from flask import (
    Blueprint, 
    request
    )
from controller import dashboard_controller

dashboard_bp = Blueprint('dashboard', __name__)