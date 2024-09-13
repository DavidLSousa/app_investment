from flask import (
    Blueprint, 
    request
    )
from controller import ticket_controller

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets', methods=['POST'])
def create_ticket():
    req = request
    
    return ticket_controller.create_ticket_controller(req)