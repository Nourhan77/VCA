from odoo import models , fields, api

class Traffic_dep (models.Model):
    _name="vca.traffic_dep"
    _description="vca department"

    traffic_department=fields.Char()
    Certificate_id=fields.One2many("vca.cert","traffic_departments")