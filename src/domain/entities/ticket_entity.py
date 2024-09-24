from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class TicketEntity:
  _nameTicket: str
  _ticket: str
  _number_of_tickets: int
  _total_value_purchased: float
  _highest_price: float
  _lowest_price: float
  _average_price: float
  _history: List[Dict[str, Any]]

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
    
    