from peewee import (
  MySQLDatabase,
  Model, 
  CharField, 
  IntegerField, 
  FloatField,
  TextField
  )
from dotenv import load_dotenv
import os
import peewee
import pymysql
import time

load_dotenv()

db = MySQLDatabase(
  os.getenv('MYSQL_DATABASE'),
  user=os.getenv('MYSQL_USER'),
  password=os.getenv('MYSQL_PASSWORD'),
  host='172.18.0.2',
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
  history = TextField(null=True)

  class Meta:
    database = db


# Connect MySQL
def connectDB(app):
  with app.app_context():
    retry_attempts = 5
    for attempt in range(retry_attempts):
      try:
        pymysql.install_as_MySQLdb()

        db.connect()
        print("Conectado ao MySQL com sucesso!")
        db.create_tables([Ticket], safe=True)
        print("Table Ticket criada com sucesso!")
        break

      except peewee.OperationalError as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        time.sleep(5)
