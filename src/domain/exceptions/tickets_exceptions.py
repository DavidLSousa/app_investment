

from src.domain.entities.ticket_entity import TicketEntity


class TicketNotFoundError(Exception):
    '''
        raise when a ticket is not found
    '''
    pass
