from unittest.mock import patch, MagicMock
import pytest

from main import app
from src.controller.ticket_controller import TicketController

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
