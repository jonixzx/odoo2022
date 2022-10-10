from psycopg2 import Date
from odoo import fields, models

class Property(models.Model):
    _name = "Property.model"
    _description = "Test Model"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()    
    date_availability =fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()