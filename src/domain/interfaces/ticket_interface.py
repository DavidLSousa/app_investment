from abc import ABC, abstractmethod

from src.domain.entities.ticket_entity import TicketEntity

class TicketInterface(ABC):
    @abstractmethod
    def get_ticket(self, ticket_name: str) -> TicketEntity | None:
        pass

    @abstractmethod
    def get_all_ticket(self) -> list[TicketEntity] | None:
        pass

    @abstractmethod
    def create_ticket(self, ticket: TicketEntity) -> None:
        pass

    @abstractmethod
    def update_ticket_sale(self, ticket_id: int, ticket: TicketEntity) -> None:
        pass

    @abstractmethod
    def update_ticket_increment(self, ticket: TicketEntity) -> None:
        pass
