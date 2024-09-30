from dataclasses import dataclass
import os, requests
import yfinance as yf

from src.domain.interfaces.name_provider_interface import NameProviderInterface

@dataclass
class NameProviderService(NameProviderInterface):
    @classmethod
    def get_ticket_name_api(cls, current_ticket) -> str:
        apis = [
            cls.use_yfinance,
            cls.use_brapi,
            cls.use_goingecko
        ]
        
        for api_func in apis:
            ticket_name = api_func(current_ticket['ticket'])
            if ticket_name is not None:
                return ticket_name
        
        raise ValueError('Ticket não encontrado')

    @classmethod
    def use_yfinance(cls, ticket_name,) -> str | None:
        ticker = yf.Ticker(ticket_name)
        ticketName = ticker.info.get('longName')

        return ticketName

    @classmethod
    def use_brapi(cls, ticket_name) -> str | None:
        try:
            url = f"https://brapi.dev/api/quote/{ticket_name}?token={os.getenv('BRAPI_TOKEN')}"
            response = requests.get(url)
            data = response.json()
            
            if 'results' in data and len(data['results']) > 0:
                return data['results'][0].get('longName')
            return None
        except Exception as err:
            raise ValueError(f"Erro ao usar a API Brapi: {str(err)}")

    @classmethod
    def use_goingecko(cls, ticket_name) -> str | None:
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{ticket_name.lower()}"
            response = requests.get(url)
            data = response.json()
            
            if 'name' in data:
                return data['name']
            return None
        except Exception as err:
            raise ValueError(f"Erro ao usar a API CoinGecko: {str(err)}")