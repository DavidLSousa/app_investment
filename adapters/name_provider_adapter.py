from dataclasses import dataclass

from src.domain.interfaces.name_provider_interface import NameProviderInterface
from src.domain.services.name_provider_service import NameProviderService


@dataclass
class NameProviderAdapter(NameProviderInterface):
    fetcher_service: NameProviderService

    async def get_ticket_name_api(self, current_ticket):
        return await self.fetcher_service.get_ticket_name_api(current_ticket)

    def use_yfinance(self, ticket_name):
        
        return self.fetcher_service.use_yfinance(ticket_name)

    def use_brapi(self, ticket_name):
        return self.fetcher_service.use_brapi(ticket_name)

    def use_goingecko(self, ticket_name):
        return self.fetcher_service.use_goingecko(ticket_name)