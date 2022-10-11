from psycopg2 import Date
from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True,default="a house")
    description = fields.Text()
    postcode = fields.Char()    
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer() 
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    active = fields.Boolean('Active', default=True)
'''type_id = fields.Many2one('property.type', string='Type',help="type of property.")'''

class Type(models.Model):
    _name = "property.type"
    _description = "type of the Property"
    name = fields.Char(required=True,default="house")



