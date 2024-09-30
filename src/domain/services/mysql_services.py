from dataclasses import dataclass

from flask import current_app

from src.domain.entities.ticket_entity import TicketEntity
from src.domain.interfaces.ticket_interface import TicketInterface
from models import Ticket

@dataclass
class MysqlServices(TicketInterface):
    def get_ticket(self, ticket_name: str) -> TicketEntity | None:
        try:
            query = Ticket.select().where(Ticket.ticket == ticket_name)
            ticket = query.dicts().get()
            
            return ticket
        
        except Exception as err:
            return None
        
    def get_all_ticket(self) -> list[TicketEntity] | None: # Implementei sem testar
        try:
            query = Ticket.select()
            tickets = query.dicts().get()
            
            return tickets
        
        except Exception as err:
            return None

    def create_ticket(self, ticket: TicketEntity) -> None:
        Ticket.create(
            nameTicket =            ticket._nameTicket,
            ticket =                ticket._ticket,
            number_of_tickets =     ticket._number_of_tickets,
            total_value_purchased = ticket._total_value_purchased,
            highest_price =         ticket._highest_price,
            lowest_price =          ticket._lowest_price,
            average_price =         ticket._average_price,
            history =               ticket._history
        )
    
    def update_ticket_sale(self, ticket_id: int, ticket: TicketEntity) -> None:
        pass
    
    def update_ticket_increment(self, ticket: TicketEntity) -> None:
        Ticket.update(
            number_of_tickets =     ticket._number_of_tickets,
            total_value_purchased = ticket._total_value_purchased,
            highest_price =         ticket._highest_price,
            lowest_price =          ticket._lowest_price,
            average_price =         ticket._average_price,
            history =               ticket._history
        ).where(
            Ticket.ticket == ticket._ticket
        ).execute()

