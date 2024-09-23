# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()

if not snapshot.database.table_exists('ticket'):
    @snapshot.append
    class Ticket(peewee.Model):
        nameTicket = CharField(max_length=255)
        ticket = CharField(max_length=255)
        number_of_tickets = IntegerField()
        total_value_purchased = FloatField()
        highest_price = FloatField()
        lowest_price = FloatField()
        average_price = FloatField()
        history = TextField(null=True)
        class Meta:
            table_name = "ticket"
else:
    print("Tabela 'ticket' já existe. Migração ignorada.")
