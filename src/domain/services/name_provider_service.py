import asyncio
from dataclasses import dataclass
import os, requests
import yfinance as yf

from src.domain.interfaces.name_provider_interface import NameProviderInterface

@dataclass
class NameProviderService(NameProviderInterface):
    @classmethod
    async def get_ticket_name_api(cls, current_ticket) -> str:
        apis = [ cls.use_yfinance, cls.use_brapi, cls.use_goingecko ]
        
        tasks = [api_func(current_ticket['ticket']) for api_func in apis]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for task in pending:
            task.cancel()

        first_completed = list(done)[0].result()
        if first_completed:
            return first_completed
        
        raise ValueError('Ticket não encontrado')

    @classmethod
    async def use_yfinance(cls, ticket_name,) -> str | None:
        ticker = yf.Ticker(ticket_name)
        ticketName = ticker.info.get('longName')

        return ticketName

    @classmethod
    async def use_brapi(cls, ticket_name) -> str | None:
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
    async def use_goingecko(cls, ticket_name) -> str | None:
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{ticket_name.lower()}"
            response = requests.get(url)
            data = response.json()
            
            if 'name' in data:
                return data['name']
            return None
        except Exception as err:
            raise ValueError(f"Erro ao usar a API CoinGecko: {str(err)}")