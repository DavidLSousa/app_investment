from flask import (
    Blueprint
)
from src.controller.ticket_controller import TicketController

tickets_bp = Blueprint('tickets', __name__)

# ============ add_page ============ 

@tickets_bp.route('/tickets/add')
def render_add_ticket_page():
    return TicketController.render_add_page()


@tickets_bp.route('/tickets/add', methods=['POST'])
def add_ticket():
    return TicketController.add_ticket_controller()

# ============ all_page ============ 

@tickets_bp.route('/tickets/all')
def render_all_ticket_page():
    return TicketController.render_all_page()


@tickets_bp.route('/tickets/all', methods=['PUT'])
def put_ticket():
    return TicketController.sale_ticket_controller()