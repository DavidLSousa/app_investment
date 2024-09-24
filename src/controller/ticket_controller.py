# transformar em uma classe
import datetime 
from nis import cat
import traceback
from flask import (
  current_app,
  render_template,
  request as req,
  Response as res
  )
from dataclasses import dataclass

from adapters.database_adapter import DatabaseAdapter
from src.domain.interfaces.ticket_interface import TicketInterface
from src.domain.services.mysql_services import MysqlServices
from src.domain.entities.ticket_entity import TicketEntity

@dataclass
class TicketController:
  MySQLDatabase: TicketInterface
  ticket: TicketEntity

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
      if not req.json:
        raise ValueError("Dados JSON não fornecidos")

      ticket = str(req.json[0]['ticket'])
      number_of_tickets = int(req.json[0]['number_of_tickets'])
      total_value_purchased = float(req.json[0]['total_value_purchased'])

      if not all([ticket, number_of_tickets, total_value_purchased]):
        raise ValueError("Dados incompletos fornecidos")

      cls.ticket = TicketEntity(
        _nameTicket='',
        _ticket=ticket,
        _number_of_tickets=number_of_tickets,
        _total_value_purchased=total_value_purchased,
        _highest_price=0,
        _lowest_price=0,
        _average_price=0,
        _history=[
          {
            'qntTickets': int(number_of_tickets),
            'valuePerTicket': float(total_value_purchased / number_of_tickets),
            'date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
          }
        ]
      )

      database_adapter = DatabaseAdapter(database=MysqlServices())
      database_adapter.create_ticket(cls.ticket)

      # OK Verificar como resolver: '"get" não é um atributo conhecido de "None"'

      # Precisa verificar se ja existe do DB, se existir, atualizar, se não existir, criar;
        # Qual a forma certa de implementar isso?

      # Implementar funções para calcular o preço médio, o preço mais alto e o preço mais baixo
        # Onde deve ser implementado? Entitie(por fazer parte do ticket) ou Controller(Pq o entitie nao tem essa função)?
      # Implementar função para adicionar o ticket no histórico
        # Creio que seja do um append no historico que ja existe, e se nao eciste cria um novo;
      # Buscar API para retornar o nome do ticker
      # O history deve ser uma lista de dicionários que tem:
        # Quantidade de tickets comprados
        # Valor pago por ticket
        # Data da compra
      # o req.json é uma lista de dicionários, logo e preciso iterar a criar um ticket para cada item da lista

      return { "status": 200 }
    
    except Exception as err:
      current_app.logger.error(f'ERRO add_ticket_controller: {err.args}')
      stack_trace = traceback.format_exc()
      current_app.logger.error(f'ERRO add_ticket_controller: {stack_trace}')
      return {'status': 500, 'error': 'Erro interno do servidor'}

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
