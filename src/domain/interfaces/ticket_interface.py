from abc import ABC, abstractmethod

from src.domain.entities.ticket_entity import TicketEntity
class TicketInterface(ABC):
    @abstractmethod
    def get_ticket(self, ticket_name: str) -> TicketEntity:
        pass

    @abstractmethod
    def get_all_ticket(self) -> list[TicketEntity]:
        pass

    @abstractmethod
    def create_ticket(self, ticket: TicketEntity) -> None:
        pass

    @abstractmethod
    def update_ticket_sale(self, dataUpdated: TicketEntity) -> None:
        pass

    @abstractmethod
    def update_ticket_increment(self, ticket: TicketEntity) -> None:
        pass

    @abstractmethod
    def delete_ticket(self, ticket_name: str) -> None:
        pass

# class TicketInterface(ABC):
#     @abstractmethod
#     def get_ticket_by_name(self, ticket_name: str) -> TicketEntity:
#         """Retrieve a ticket by its name."""

#     @abstractmethod
#     def get_all_tickets(self) -> list[TicketEntity]:
#         """Retrieve all tickets."""

#     @abstractmethod
#     def create_ticket(self, ticket: TicketEntity) -> None:
#         """Create a new ticket."""

#     @abstractmethod
#     def update_ticket_after_sale(self, data_updated: TicketEntity) -> None:
#         """Update a ticket after a sale."""

#     @abstractmethod
#     def update_ticket_after_increment(self, ticket: TicketEntity) -> None:
#         """Update a ticket after an increment."""

#     @abstractmethod
#     def delete_ticket_by_id(self, ticket_id: int) -> None:
#         """Delete a ticket by its id."""

