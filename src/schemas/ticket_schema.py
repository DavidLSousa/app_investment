
from marshmallow import Schema, fields


class TicketSchema(Schema):
    ticket = fields.Str(required=True)
    number_of_tickets = fields.Int(required=True, strict=True, validate=lambda n: n > 0)
    total_value_purchased = fields.Float(required=True, strict=True, validate=lambda v: v > 0)