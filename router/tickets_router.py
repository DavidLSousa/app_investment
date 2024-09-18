from flask import (
    Blueprint, 
    request
    )
from controller.ticket_controller import TicketController

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets')
def get_ticket():
    return TicketController.render_page()

@tickets_bp.route('/tickets', methods=['POST'])
def add_ticket():
    pass

@tickets_bp.route('/tickets', methods=['DELETE'])
def delete_ticket():
    pass

@tickets_bp.route('/tickets', methods=['PUT'])
def put_ticket():
    pass