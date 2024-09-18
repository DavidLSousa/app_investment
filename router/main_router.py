from flask import (
    Blueprint,
    render_template
    )

main_page_bp = Blueprint('main', __name__)

@main_page_bp.route('/', methods=['GET'])
def render_main_page():
    return render_template('main_page.html')
