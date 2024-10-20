import asyncio
import bleach
import datetime, traceback

from flask import (
    current_app,
    render_template,
    request as req,
    jsonify
)
from dataclasses import dataclass

from adapters.database_adapter import DatabaseAdapter
from adapters.name_provider_adapter import NameProviderAdapter

from src.domain.services.name_provider_service import NameProviderService
from src.domain.services.mysql_services import MysqlServices

from src.domain.exceptions.tickets_exceptions import TicketNotFoundError
from src.domain.entities.ticket_entity import TicketEntity

@dataclass
class TicketController:
    database_adapter = DatabaseAdapter(database=MysqlServices())
    info_fetcher_adapter = NameProviderAdapter(fetcher_service=NameProviderService())

    @classmethod
    def render_all_page(cls):
        try:
            tickets = cls.database_adapter.get_all_ticket()
            
            tickets_formatted = cls.__format_tickets_for_page(tickets)

            return render_template('all_tickets_page.html', title_page='Meus Ativos', tickets=tickets_formatted), 200
        
        except ValueError as err:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ERRO render_all_page: {stack_trace}')
            return jsonify({'error': str(err)}), 500  

        except Exception as e:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ERRO inesperado em render_all_page: {stack_trace}')
            return jsonify({'error': 'Erro interno do servidor'}), 500

    @classmethod
    def render_add_page(cls):
        try:
            return render_template('add_tickets_page.html', title_page='Adicionar Ativos'), 200
        
        except ValueError as err:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ERRO render_add_page: {stack_trace}')
            return jsonify({'error': 'Erro interno do servidor'}), 500

    @classmethod
    def add_ticket_controller(cls):
        try:
            if not req.json:
                raise ValueError("Dados JSON não fornecidos")


            if req.json is not None:
                for current_ticket in req.json:
                    sanitize_data = cls.__sanitize_data_add_ticket(current_ticket)

                    try:
                        check_ticket_in_db = cls.database_adapter.get_ticket(sanitize_data['ticket'])
                    
                        cls.__handle_update_ticket(sanitize_data, check_ticket_in_db)
                    except TicketNotFoundError:
                        asyncio.run(cls.__handle_create_ticket(sanitize_data))


            return jsonify({'status': 200, 'success': 'Tudo certo'}), 200
        
        except Exception as err:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ERRO add_ticket_controller: {stack_trace}')
            return jsonify({'error': 'Erro interno do servidor'}), 500

    @classmethod
    def sale_ticket_controller(cls):  
        try:
            if not req.json:
                raise ValueError("Dados JSON não fornecidos")
            
            sanitazed_data = cls.__sanitize_data_sale_ticket(req.json)

            db_ticket = cls.database_adapter.get_ticket(sanitazed_data['ticket'])
            
            number_of_tickets_updated = int(db_ticket.number_of_tickets) - int(sanitazed_data['number_of_sale_tickets'])
            if number_of_tickets_updated == 0: 
                cls.database_adapter.delete_ticket(db_ticket.nameTicket)
                return jsonify({'status': 200, 'success': 'Tudo certo' }), 200

            updated_ticket = TicketEntity(
                nameTicket=             db_ticket.nameTicket,
                ticket=                 db_ticket.ticket,
                _number_of_tickets=     number_of_tickets_updated,
                _total_value_purchased= db_ticket.total_value_purchased - float(sanitazed_data['total_sale_value']),
                _highest_price=         db_ticket._highest_price,
                _lowest_price=          db_ticket._lowest_price,
                _average_price=         db_ticket._average_price,
                history=                db_ticket.history + [{ # type: ignore
                    'number_of_sale_tickets': int(sanitazed_data['number_of_sale_tickets']),
                    'total_sale_value': float(sanitazed_data['total_sale_value']),
                    'date': cls.__get_datetime()
                }]
            )

            cls.database_adapter.update_ticket_sale(updated_ticket)

            return jsonify({'status': 200, 'success': 'Tudo certo' }), 200

        except ValueError as err:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ValueError edit_ticket_controller: {stack_trace}')
            return jsonify({'error': str(err)}), 500
        
        except Exception:
            stack_trace = traceback.format_exc()
            current_app.logger.error(f'ERRO edit_ticket_controller: {stack_trace}')
            return jsonify({'error': 'Erro interno do servidor'}), 500

    # =========================== Private methods =========================== #
    @classmethod
    async def __handle_create_ticket(cls, current_data_ticket) -> None:
        ticket = str(current_data_ticket['ticket'])
        number_of_tickets = int(current_data_ticket['number_of_tickets'])
        total_value_purchased = float(current_data_ticket['total_value_purchased'])

        price_metrics = cls.__get_price_metrics(current_data_ticket)
        name_ticket = await cls.info_fetcher_adapter.get_ticket_name_api(current_data_ticket)

        new_ticket = TicketEntity(
            nameTicket=             name_ticket,
            ticket=                 ticket,
            _number_of_tickets=     number_of_tickets,
            _total_value_purchased= total_value_purchased,
            _highest_price=         price_metrics['highest_price'],
            _lowest_price=          price_metrics['lowest_price'],
            _average_price=         price_metrics['average_price'],
            history=[
                {
                    'qntTickets': number_of_tickets,
                    'valuePerTicket': total_value_purchased / number_of_tickets,
                    'date': cls.__get_datetime()
                }
            ]
        )

        cls.database_adapter.create_ticket(new_ticket)

    @classmethod
    def __handle_update_ticket(cls, new_data_ticket: dict, db_ticket: TicketEntity) -> None:
        updated_number_of_tickets = int(db_ticket.number_of_tickets) + int(new_data_ticket['number_of_tickets'])
        updated_total_value_purchased = float(db_ticket.total_value_purchased) + float(new_data_ticket['total_value_purchased'])

        price_metrics = cls.__get_price_metrics(new_data_ticket, db_ticket)

        updated_ticket = TicketEntity(
            nameTicket=             db_ticket.nameTicket,
            ticket=                 db_ticket.ticket,
            _number_of_tickets=     updated_number_of_tickets,
            _total_value_purchased= updated_total_value_purchased,
            _highest_price=         price_metrics['highest_price'],
            _lowest_price=          price_metrics['lowest_price'],
            _average_price=         price_metrics['average_price'],
            history=                db_ticket.history + [ # type: ignore
                {
                    'qntTickets': new_data_ticket['number_of_tickets'],
                    'valuePerTicket': float(new_data_ticket['total_value_purchased']) / int(new_data_ticket['number_of_tickets']),
                    'date': cls.__get_datetime()
                }
            ]
        )

        cls.database_adapter.update_ticket_increment(updated_ticket)

    @classmethod
    def __get_price_metrics(
        cls, 
        new_data_ticket: dict, 
        db_ticket: TicketEntity | None = None
    ) -> dict[str, float]:
        new_total_value_purchased = float(new_data_ticket['total_value_purchased'])
        new_number_of_tickets = float(new_data_ticket['number_of_tickets'])
        new_price = new_total_value_purchased / new_number_of_tickets

        if db_ticket is None:
            return {
                'average_price': new_price,
                'highest_price': new_price,
                'lowest_price': new_price
            }
        
        total_tickets = db_ticket.number_of_tickets + new_number_of_tickets
        total_value_purchased = db_ticket.total_value_purchased + new_total_value_purchased
        new_average_price = total_value_purchased / total_tickets
        
        highest_price = max(db_ticket._highest_price, new_price)
        lowest_price = min(db_ticket._lowest_price, new_price)

        return {
            'average_price': new_average_price,
            'highest_price': highest_price,
            'lowest_price': lowest_price
        }

    @classmethod
    def __get_datetime(cls):
        return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    @classmethod
    def __format_tickets_for_page(cls, tickets: list[TicketEntity]) -> list[TicketEntity]:
        formatted_tickets = []
        for ticket in tickets:
            formatted_ticket = TicketEntity(
                nameTicket=             ticket.nameTicket,
                ticket=                 ticket.ticket,
                _number_of_tickets=     ticket.number_of_tickets,
                _highest_price=         float("{:.2f}".format(float(ticket.highest_price))),
                _lowest_price=          float("{:.2f}".format(float(ticket.lowest_price))),
                _average_price=         float("{:.2f}".format(float(ticket.average_price))),
                _total_value_purchased= float("{:.2f}".format(float(ticket.total_value_purchased))),
                history=                []
            )
                
            formatted_tickets.append(formatted_ticket)
            
        return formatted_tickets
    
    # ================================ Validations ================================ #
    @classmethod
    def __sanitize_data_sale_ticket(cls, dataJson):
        dataJsonSanatized = {
            'ticket': bleach.clean(dataJson['ticket']),
            'number_of_sale_tickets': bleach.clean(str(dataJson['number_of_sale_tickets'])),
            'total_sale_value': bleach.clean(str(dataJson['total_sale_value']))
        }

        return dataJsonSanatized

    @classmethod
    def __sanitize_data_add_ticket(cls, dataJson):
        dataJsonSanatized = {
            'ticket': bleach.clean(dataJson['ticket']),
            'number_of_tickets': bleach.clean(str(dataJson['number_of_tickets'])),
            'total_value_purchased': bleach.clean(str(dataJson['total_value_purchased']))
        }

        return dataJsonSanatized
