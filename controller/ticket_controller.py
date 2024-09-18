# transformar em uma classe
from flask import render_template
from dataclasses import dataclass

@dataclass
class TicketController:
    @classmethod
    def render_page(cls):
        # Pegar info do db e passar para renderizar a pagina com os dados dos tickets do db
        return render_template('tickets_page.html')

    @classmethod
    def add_ticket_controller(cls):
        pass

    @classmethod
    def delete_ticket_controller(cls):
        pass

    @classmethod
    def put_ticket_controller(cls):
        pass