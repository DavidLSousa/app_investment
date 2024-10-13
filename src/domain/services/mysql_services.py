from dataclasses import dataclass

from flask import current_app

from src.domain.exceptions.tickets_exceptions import TicketNotFoundError

from src.domain.entities.ticket_entity import TicketEntity
from src.domain.interfaces.ticket_interface import TicketInterface
from models import Ticket

@dataclass
class MysqlServices(TicketInterface):
    def get_ticket(self, ticket_name: str) -> TicketEntity:
        try:
            query = Ticket.select().where(Ticket.ticket == ticket_name)
            ticket_dict = query.dicts().get()

            return TicketEntity(
                    nameTicket=             ticket_dict['nameTicket'],
                    ticket=                 ticket_dict['ticket'],
                    _number_of_tickets=     ticket_dict['number_of_tickets'],
                    _total_value_purchased= ticket_dict['total_value_purchased'],
                    _highest_price=         ticket_dict['highest_price'],
                    _lowest_price=          ticket_dict['lowest_price'],
                    _average_price=         ticket_dict['average_price'],
                    history=                ticket_dict['history']
                )
        
        except Exception as err:
            raise TicketNotFoundError(f'Ticket {ticket_name} não encontrado.')
        
    def get_all_ticket(self) -> list[TicketEntity]:
        try:
            query = Ticket.select()
            
            tickets = [
                TicketEntity(
                    nameTicket=             ticket['nameTicket'],
                    ticket=                 ticket['ticket'],
                    _number_of_tickets=     ticket['number_of_tickets'],
                    _total_value_purchased= ticket['total_value_purchased'],
                    _highest_price=         ticket['highest_price'],
                    _lowest_price=          ticket['lowest_price'],
                    _average_price=         ticket['average_price'],
                    history=                ticket['history']
                )
                for ticket in query.dicts()
            ]
            
            return tickets
        
        except Exception as err:
            raise TicketNotFoundError(f'Nenhum ticket encontrado.')

    def create_ticket(self, ticket: TicketEntity) -> None:
        Ticket.create(
            nameTicket =            ticket.nameTicket,
            ticket =                ticket.ticket,
            number_of_tickets =     ticket._number_of_tickets,
            total_value_purchased = ticket._total_value_purchased,
            highest_price =         ticket._highest_price,
            lowest_price =          ticket._lowest_price,
            average_price =         ticket._average_price,
            history =               ticket.history
        )
    
    def update_ticket_sale(self, ticket_updated: TicketEntity) -> None:
        Ticket.update(
            number_of_tickets =     ticket_updated._number_of_tickets,
            total_value_purchased = ticket_updated._total_value_purchased,
            history =               ticket_updated.history
        ).where(
            Ticket.ticket == ticket_updated.ticket
        ).execute()
    
    def update_ticket_increment(self, ticket: TicketEntity) -> None:
        Ticket.update(
            number_of_tickets =     ticket._number_of_tickets,
            total_value_purchased = ticket._total_value_purchased,
            highest_price =         ticket._highest_price,
            lowest_price =          ticket._lowest_price,
            average_price =         ticket._average_price,
            history =               ticket.history
        ).where(
            Ticket.ticket == ticket.ticket
        ).execute()

    def delete_ticket(self, ticket_name: str) -> None:
        Ticket.delete().where(Ticket.nameTicket == ticket_name).execute() 
