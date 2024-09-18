from peewee import *

db = MySQLDatabase(
    'ticketsDB',
    user='MYSQL_USER',  
    password='MYSQL_PASSWORD',
    host='localhost',    
    port=3306            
)

class Ticket(Model):
    nameTicket = CharField()
    ticket = CharField()
    number_of_tickets = IntegerField()
    total_value_purchased = FloatField()
    highest_price = FloatField()
    lowest_price = FloatField()
    average_price = FloatField()
    average_price = FloatField()

    class Meta:
        database = db

db.connect()
db.create_tables([Ticket])