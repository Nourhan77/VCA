from odoo import models , fields, api

class Customer(models.Model):
    _name="vca.customers"
    _description="VCA Customers"

    name=fields.Char(required=True)
    cert_id=fields.One2many("vca.cert","Customer_id")
    phone=fields.Char()