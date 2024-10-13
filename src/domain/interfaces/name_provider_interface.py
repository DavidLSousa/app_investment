from abc import ABC, abstractmethod

class NameProviderInterface(ABC):
    @abstractmethod
    async def get_ticket_name_api(cls, current_ticket):
        pass

    @abstractmethod
    def use_yfinance(cls, ticket_name):
        pass

    @abstractmethod
    def use_brapi(cls, ticket_name):
        pass

    @abstractmethod
    def use_goingecko(cls, ticket_name):
        pass