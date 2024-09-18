from flask import (
    Blueprint, 
    request
    )
from controller.ticket_controller import TicketController

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets')
def get_ticket():
    # Pegar info do db e passar para renderizar a pagina com os dados dos tickets do db
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