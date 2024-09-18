from flask import (
    Blueprint, 
    request
    )
from controller import news_controller

news_bp = Blueprint('news', __name__)