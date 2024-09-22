# transformar em uma classe
from flask import render_template
from dataclasses import dataclass

from models import Ticket


@dataclass
class TicketController:
  @classmethod
  def render_add_page(cls):
    # Pegar info do db e passar para renderizar a pagina com os dados dos tickets do db
    return render_template('add_tickets_page.html', title_page='Adicionar Ativos')

  @classmethod
  def render_all_page(cls):
    test = [
      {
        'ticket': 'ITSA4',
        'nameTicket': 'Itausa',
        'average_price': 8.51,
        'number_of_tickets': 55,
        'total_value_purchased': 602.25
      },
      {
        'ticket': 'PETR3',
        'nameTicket': 'Petrobras',
        'average_price': 30.00,
        'number_of_tickets': 20,
        'total_value_purchased': 600.00
      },
      {
        'ticket': 'VALE3',
        'nameTicket': 'Vale',
        'average_price': 75.00,
        'number_of_tickets': 10,
        'total_value_purchased': 750.00
      }
    ]

    return render_template('all_tickets_page.html', title_page='Meus Ativos', tickets=test)

  @classmethod
  def add_ticket_controller(cls):
    pass

  @classmethod
  def delete_ticket_controller(cls):
    pass

  @classmethod
  def put_ticket_controller(cls):
    pass
