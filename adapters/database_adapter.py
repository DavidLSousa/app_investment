from dataclasses import dataclass

from src.domain.entities.ticket_entity import TicketEntity
from src.domain.interfaces.ticket_interface import TicketInterface

@dataclass
class DatabaseAdapter(TicketInterface):
    database: TicketInterface 

    def get_ticket(self, ticket_name: str) -> TicketEntity:
        return self.database.get_ticket(ticket_name)
    
    def get_all_ticket(self) -> list[TicketEntity]:
        return self.database.get_all_ticket()
    
    def create_ticket(self, ticket: TicketEntity):
        self.database.create_ticket(ticket)
    
    def update_ticket_sale(self, dataUpdated: TicketEntity): 
        self.database.update_ticket_sale(dataUpdated)  
    
    def update_ticket_increment(self, ticket: TicketEntity):
        self.database.update_ticket_increment(ticket)

    def delete_ticket(self, ticket_name: str):
        self.database.delete_ticket(ticket_name)
