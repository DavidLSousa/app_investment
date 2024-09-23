# transformar em uma classe
from nis import cat
from flask import (
  render_template,
  request as req,
  Response as res
  )
from dataclasses import dataclass

@dataclass
class TicketController:
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

    try:
      return render_template('all_tickets_page.html', title_page='Meus Ativos', tickets=test)
    
    except ValueError as err:
      print(f'ERROR render_all_page: {err}')
      return { 'status': 500}
  
  @classmethod
  def render_add_page(cls):
    # Pegar info do db e passar para renderizar a pagina com os dados dos tickets do db
  
    try:
      return render_template('add_tickets_page.html', title_page='Adicionar Ativos')
    
    except ValueError as err:
      print(f'ERROR render_add_page: {err}')
      return { 'status': 500}

  @classmethod
  def add_ticket_controller(cls):
    try:
      print(f'Req Body:  {req.json}')

      return { "status": 200 }
    
    except ValueError as err:
      print(f'ERROR add_ticket_controller: {err}')
      return { 'status': 500 }

  @classmethod
  def delete_ticket_controller(cls, ticker):
    try:
      print(f'Ticker del:  {ticker}')

      return { "status": 200 }
    
    except ValueError as err:
      print(f'ERROR delete_ticket_controller: {err}')
      return { 'status': 500 }

  @classmethod
  def edit_ticket_controller(cls, ticker):
    try:
      print(f'Ticker edit:  {ticker}')

      return { "status": 200 }
    
    except ValueError as err:
      print(f'ERROR edit_ticket_controller: {err}')
      return { 'status': 500 }
