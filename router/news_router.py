from flask import (
  Blueprint, 
  request
  )
from src.controller import news_controller

news_bp = Blueprint('news', __name__)