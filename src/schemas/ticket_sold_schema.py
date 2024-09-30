
from marshmallow import Schema, fields


class TicketSoldSchema(Schema):
    ticket = fields.Str(required=True)
    number_of_sale_tickets = fields.Int(required=True, strict=True, validate=lambda n: n > 0)
    total_sale_value = fields.Float(required=True, strict=True, validate=lambda v: v > 0)