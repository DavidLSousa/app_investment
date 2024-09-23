from dataclasses import dataclass

from domain.entities.ticket_entity import TicketEntity
from domain.services.ticket_services import TicketServices
from src.domain.interfaces.ticket_interface import TicketInterface

@dataclass
class DatabaseAdapter(TicketInterface):
  def __init__(self, database: TicketServices):
    self.database = database

  def get_ticket(self, ticket_id: int):
    return self.database.get_ticket(ticket_id)
  
  def get_all_ticket(self):
    return self.database.get_all_ticket()
  
  def create_ticket(self, ticket: TicketEntity):
    return self.database.create_ticket(ticket)
  
  def update_ticket(self, ticket_id: int, ticket: TicketEntity):
    return self.database.update_ticket(ticket_id, ticket)
  
  def delete_ticket(self, ticket_id: int):
    return self.database.delete_ticket(ticket_id)
