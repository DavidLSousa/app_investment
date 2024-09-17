from flask import (
    Blueprint, 
    request
    )
from controller import ticket_controller

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets')
def get_ticket():
    pass

@tickets_bp.route('/tickets', methods=['POST'])
def add_ticket():
    return ticket_controller.add_ticket_controller(request)

@tickets_bp.route('/tickets', methods=['DELETE'])
def delete_ticket():
    pass

@tickets_bp.route('/tickets', methods=['PUT'])
def put_ticket():
    pass