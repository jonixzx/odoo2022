from odoo import fields, models

class Type(models.Model):
    _name = "property.type"
    _description = "type of the Property"
    name = fields.Char(required=True,default="house")