from dataclasses import dataclass

from src.domain.entities.ticket_entity import TicketEntity
from src.domain.interfaces.ticket_interface import TicketInterface
from models import Ticket

@dataclass
class MysqlServices(TicketInterface):
    def get_ticket(self, ticket_name: str):
        try:
            query = Ticket.select().where(Ticket.ticket == ticket_name)
            ticket = query.dicts().get()
            
            return ticket
        
        except Exception as err:
            return None
    # class TicketNotFoundError(Exception):
    #     pass

    # def get_ticket(ticket_id: int) -> TicketEntity:
    #     ticket = find_ticket_in_database(ticket_id)  # Supondo que essa função busque o ticket
    #     if ticket is None:
    #         raise TicketNotFoundError(f'Ticket com ID {ticket_id} não encontrado.')
    #     return ticket
        
    def get_all_ticket(self):
        try:
            query = Ticket.select()
            tickets = list(query.dicts())
            
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
    
    def update_ticket_sale(self, ticket_updated: TicketEntity) -> None:
        Ticket.update(
            number_of_tickets =     ticket_updated._number_of_tickets,
            total_value_purchased = ticket_updated._total_value_purchased,
            history =               ticket_updated._history
        ).where(
            Ticket.ticket == ticket_updated._ticket
        ).execute()
    
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

    def delete_ticket(self, ticket_id: int) -> None:
        Ticket.delete().where(Ticket.id == ticket_id).execute() # type: ignore
