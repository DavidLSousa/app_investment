from unittest.mock import patch, MagicMock
import pytest
import json

from main import app
from src.controller.ticket_controller import TicketController

# ============================== render tests =============================== #

def test_render_all_page():
    # Arrange
    mock_tickets = [
        {
            'ticket': 'AAPL',
            'nameTicket': 'Apple Inc.',
            'number_of_tickets': 10,
            'total_value_purchased': 1500.00,
            'highest_price': 160.00,
            'lowest_price': 140.00,
            'average_price': 150.00
        }
    ]
    
    # Act
    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_all_ticket.return_value = mock_tickets
        with patch('src.controller.ticket_controller.render_template') as mock_render:
            mock_render.return_value = 'rendered_template'
            result = TicketController.render_all_page()
    
    # Assert
    mock_db.get_all_ticket.assert_called_once()
    mock_render.assert_called_once_with(
        'all_tickets_page.html',
        title_page='Meus Ativos',
        tickets=[{
            'ticket': 'AAPL',
            'nameTicket': 'Apple Inc.',
            'highest_price': '160.00',
            'lowest_price': '140.00',
            'average_price': '150.00',
            'number_of_tickets': 10,
            'total_value_purchased': '1500.00'
        }]
    )
    assert result[0] == 'rendered_template'

def test_render_all_page_no_tickets():
    # Arrange
    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_all_ticket.return_value = None
        with app.app_context():  
            with patch('src.controller.ticket_controller.current_app') as mock_app:
                mock_app.logger = MagicMock()
                result = TicketController.render_all_page()
    
    # Assert
    mock_db.get_all_ticket.assert_called_once()
    mock_app.logger.error.assert_called_once()
    assert result[1] == 500 
    assert isinstance(result[0].data.decode('utf-8'), str) 
    assert 'error' in result[0].data.decode('utf-8') 

def test_render_all_page_exception():
    # Arrange
    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_all_ticket.side_effect = Exception("Database error")
        with app.app_context():  
            with patch('src.controller.ticket_controller.current_app') as mock_app:
                mock_app.logger = MagicMock()
                result = TicketController.render_all_page()
    
    # Assert
    mock_db.get_all_ticket.assert_called_once()
    mock_app.logger.error.assert_called_once()
    assert result[1] == 500 
    assert isinstance(result[0].data.decode('utf-8'), str) 
    assert 'error' in result[0].data.decode('utf-8') 

# ============================== backend tests ============================== #

def test_add_ticket_controller_success():
    mock_ticket_data = [
        {
            'ticket': 'AAPL',
            'number_of_tickets': 10,
            'total_value_purchased': 1500.00
        }
    ]

    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_ticket.return_value = None  # Simula que o ticket não existe
        with app.test_request_context(json=mock_ticket_data):
            response = TicketController.add_ticket_controller()

    assert response[1] == 200
    assert json.loads(response[0].data) == {'status': 200, 'success': 'Tudo certo'}

def test_add_ticket_controller_ticket_exists():
    mock_ticket_data = [
        {
            'ticket': 'AAPL',
            'number_of_tickets': 10,
            'total_value_purchased': 1500.00
        }
    ]

    mock_db_ticket = {
        'ticket': 'AAPL',
        'nameTicket': 'Apple Inc.',
        'number_of_tickets': 10,
        'total_value_purchased': 1500.00,
        'highest_price': 160.00,
        'lowest_price': 140.00,
        'average_price': 150.00,
        'history': "[{ 'qntTickets': 10, 'valuePerTicket': 150.00, 'date': '01/01/2024 00:00:00' }]"
    }

    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_ticket.return_value = mock_db_ticket  # Simula que o ticket já existe
        with app.test_request_context(json=mock_ticket_data):
            response = TicketController.add_ticket_controller()

    assert response[1] == 200
    assert json.loads(response[0].data) == {'status': 200, 'success': 'Tudo certo'}

def test_add_ticket_controller_no_json():
    with app.test_request_context():
        response = TicketController.add_ticket_controller()

    assert response[1] == 500
    assert 'error' in json.loads(response[0].data)

def test_sale_ticket_controller_success():
    mock_sale_data = {
        'ticket': 'AAPL',
        'number_of_sale_tickets': 5,
        'total_sale_value': 800.00
    }

    mock_db_ticket = {
        'ticket': 'AAPL',
        'nameTicket': 'Apple Inc.',
        'number_of_tickets': 10,
        'total_value_purchased': 1500.00,
        'highest_price': 160.00,
        'lowest_price': 140.00,
        'average_price': 150.00,
        'history': '[]'
    }

    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_ticket.return_value = mock_db_ticket  # Simula que o ticket existe
        with app.test_request_context(json=mock_sale_data):
            response = TicketController.sale_ticket_controller()

    assert response[1] == 200
    assert json.loads(response[0].data) == {'status': 200, 'success': 'Tudo certo'}

def test_sale_ticket_controller_ticket_not_found():
    mock_sale_data = {
        'ticket': 'AAPL',
        'number_of_sale_tickets': 5,
        'total_sale_value': 800.00
    }

    with patch('src.controller.ticket_controller.TicketController.database_adapter') as mock_db:
        mock_db.get_ticket.return_value = None  # Simula que o ticket não existe
        with app.test_request_context(json=mock_sale_data):
            response = TicketController.sale_ticket_controller()

    assert response[1] == 500
    assert 'error' in json.loads(response[0].data)

def test_sale_ticket_controller_no_json():
    with app.test_request_context(json={}):
        response = TicketController.sale_ticket_controller()

    assert response[1] == 500
    assert 'error' in json.loads(response[0].data)