from dataclasses import dataclass, field
from typing import Any, Dict, List
import uuid

@dataclass
class TicketEntity:
    nameTicket: str
    ticket: str
    _number_of_tickets: int
    _total_value_purchased: float
    _highest_price: float
    _lowest_price: float
    _average_price: float
    history: List[Dict[str, Any]]
    id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # def __post_init__(self): # Isso lança erros que n sei pq
    #     self.nameTicket = self.nameTicket
    #     self.ticket = self.ticket
    #     self.number_of_tickets = self._number_of_tickets
    #     self.total_value_purchased = self._total_value_purchased
    #     self.highest_price = self._highest_price
    #     self.lowest_price = self._lowest_price
    #     self.average_price = self._average_price
    #     self.history = self.history

    @property
    def number_of_tickets(self):
        return self._number_of_tickets
    @number_of_tickets.setter
    def number_of_tickets(self, value):
        if (value > 0):
            self._number_of_tickets = value
            return
        
        raise ValueError("O número de tickets deve ser maior que 0")

    @property
    def total_value_purchased(self):
        return self._total_value_purchased
    @total_value_purchased.setter
    def total_value_purchased(self, value):
        if (value > 0):
            self._total_value_purchased = value
            return
        
        raise ValueError("O valor total de compra deve ser maior que 0")
    
    @property
    def highest_price(self):
        return self._highest_price
    @highest_price.setter
    def highest_price(self, value):
        if (value > 0):
            self._highest_price = value
            return
        
        raise ValueError("O valor de compra deve ser maior que 0")
    
    @property
    def lowest_price(self):
        return self._lowest_price
    @lowest_price.setter
    def lowest_price(self, value):
        if (value > 0):
            self._lowest_price = value
            return
        
        raise ValueError("O valor de compra deve ser maior que 0")
    
    @property
    def average_price(self):
        return self._average_price
    @average_price.setter
    def average_price(self, value):
        if (value > 0):
            self._average_price = value
            return
        
        raise ValueError("O valor de compra deve ser maior que 0")
