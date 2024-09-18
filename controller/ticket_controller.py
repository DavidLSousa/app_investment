# transformar em uma classe
from flask import render_template
from dataclasses import dataclass

@dataclass
class TicketController:
    @classmethod
    def render_page(cls):
        return render_template('tickets_page.jinja')

    @classmethod
    def add_ticket_controller(cls):
        pass

    @classmethod
    def delete_ticket_controller(cls):
        pass

    @classmethod
    def put_ticket_controller(cls):
        pass