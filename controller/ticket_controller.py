# transformar em uma classe
from flask import render_template
from dataclasses import dataclass


@dataclass
class TicketController:
  @classmethod
  def render_add_page(cls):
    # Pegar info do db e passar para renderizar a pagina com os dados dos tickets do db
    return render_template('add_tickets_page.html', title_page='Adicionar Ativos')

  @classmethod
  def render_all_page(cls):
    return render_template('all_tickets_page.html', title_page='Meus Ativos')

  @classmethod
  def add_ticket_controller(cls):
    pass

  @classmethod
  def delete_ticket_controller(cls):
    pass

  @classmethod
  def put_ticket_controller(cls):
    pass
