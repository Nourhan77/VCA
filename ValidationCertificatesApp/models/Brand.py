
from odoo import models , fields, api

class brands (models.Model):
    _name="vca.brands"
    description="VCA Brands"
    brand_name=fields.Char(required=True)
    brand_id = fields.One2many("vca.cert","brand")