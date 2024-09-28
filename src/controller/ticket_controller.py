import yfinance as yf
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

  database_adapter = DatabaseAdapter(database=MysqlServices())

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

      for current_ticket in req.json:
        check_ticket_in_db = cls.database_adapter.get_ticket(current_ticket['ticket']) # get_ticket recebe um int no adapter

        current_app.logger.info(f'check_ticket_in_db: {check_ticket_in_db}')
        
        if check_ticket_in_db:
          cls.__handle_update_ticket(current_ticket, check_ticket_in_db)
        else:
          cls.__handle_create_ticket(current_ticket)

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
      # Não implementar até ajustar o front
      print(f'Ticker edit:  {ticker}')

      return { "status": 200 }
    
    except ValueError as err:
      print(f'ERROR edit_ticket_controller: {err}')
      return { 'status': 500 }

  # =========================== Private methods =========================== #
  @classmethod
  def __handle_create_ticket(cls, current_ticket):
    ticket = str(current_ticket['ticket'])
    number_of_tickets = int(current_ticket['number_of_tickets'])
    total_value_purchased = float(current_ticket['total_value_purchased'])
      
    cls.ticket = TicketEntity(
      _nameTicket=            cls.__get_ticket_name_api(current_ticket),
      _ticket=                ticket,
      _number_of_tickets=     number_of_tickets,
      _total_value_purchased= total_value_purchased,
      _highest_price=         cls.__get_price_metrics(current_ticket)['highest_price'],
      _lowest_price=          cls.__get_price_metrics(current_ticket)['lowest_price'],
      _average_price=         cls.__get_price_metrics(current_ticket)['average_price'],
      _history=[
        {
          'qntTickets': number_of_tickets,
          'valuePerTicket': total_value_purchased / number_of_tickets,
          'date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
      ]
    )

    cls.database_adapter.create_ticket(cls.ticket)
  
  @classmethod
  def __handle_update_ticket(cls, new_ticket, db_ticket):
    # Se esta aqui é pq ja foi achado no banco de dados
    # check_ticket_in_db é o que foi obtido no BD
    # atualizar o check_ticket_in_db com os novos dados do current_ticket
      # add ao histico os dados do current_ticket
        # append no historico
      # atualizar o preço médio, o preço mais alto e o preço mais baixo
      #  atualizar o valor total investido
    # salvar no BD o ticket atualizado

    new_number_of_tickets = int(db_ticket['number_of_tickets']) + int(new_ticket['number_of_tickets'])
    new_total_value_purchased = float(db_ticket['total_value_purchased']) + float(new_ticket['total_value_purchased'])
    
    updated_ticket = TicketEntity(
      _nameTicket=            db_ticket['nameTicket'],
      _ticket=                db_ticket['ticket'],
      _number_of_tickets=     new_number_of_tickets,
      _total_value_purchased= new_total_value_purchased,
      _highest_price=         cls.__get_price_metrics(new_ticket)['highest_price'],
      _lowest_price=          cls.__get_price_metrics(new_ticket)['lowest_price'],
      _average_price=         cls.__get_price_metrics(new_ticket)['average_price'],
      _history=               db_ticket.history.append(
        {
          'qntTickets': new_ticket['number_of_tickets'],
          'valuePerTicket': new_ticket['total_value_purchased'] / new_ticket['number_of_tickets'],
          'date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
      )
    )

    current_app.logger.info(f'updated_ticket: {updated_ticket}')

    cls.database_adapter.update_ticket_increment(updated_ticket)
  
  @classmethod
  def __get_ticket_name_api(cls, current_ticket) -> str:    
    ticker = yf.Ticker(current_ticket['ticket'])
    ticketName = ticker.info.get('longName')

    if ticketName == None:
      raise ValueError('Ticket não encontrado')

    return ticketName
  
  @classmethod
  def __get_price_metrics(cls, new_ticket, db_ticket=None):
    new_total_value_purchased = float(new_ticket['total_value_purchased'])
    new_number_of_tickets = float(new_ticket['number_of_tickets'])

    if not db_ticket:
      first_metric = new_total_value_purchased / new_number_of_tickets
      return {
        'average_price': first_metric,
        'highest_price': first_metric,
        'lowest_price': first_metric
      }
    
    total_tickets = db_ticket['number_of_tickets'] + new_number_of_tickets
    total_value_purchased = db_ticket['total_value_purchased'] + new_total_value_purchased
    
    new_average_price = total_value_purchased / total_tickets
    
    new_price = new_total_value_purchased / new_number_of_tickets
    
    highest_price = max(db_ticket['highest_price'], new_price)
    lowest_price = min(db_ticket['lowest_price'], new_price)

    return {
      'average_price': new_average_price,
      'highest_price': highest_price,
      'lowest_price': lowest_price
    }