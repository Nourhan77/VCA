from odoo import models , fields, api

class Certificate_type (models.Model):
    _name="vca.cert_types"
    _description="VCA Certificate types"

    cert_type=fields.Char()
    cert_id=fields.One2many("vca.cert","traffic_departments")