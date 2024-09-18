from flask import Blueprint
from view.main_view import MainView

main_page_bp = Blueprint('main', __name__)

@main_page_bp.route('/', methods=['GET'])
def render_main_page():
    return MainView.render_main_page()
