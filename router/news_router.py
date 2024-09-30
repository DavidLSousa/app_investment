from flask import (
    Blueprint
    )
from src.controller import news_controller

news_bp = Blueprint('news', __name__)