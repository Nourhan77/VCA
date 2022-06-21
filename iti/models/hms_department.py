from odoo import models , fields

class HMSDepartment (models.Model):
    _name="hms.department"
    _description="HMS Lab cont."
    



    department_Name=fields.Char(required=True)
    department_capacity=fields.Integer()
    Is_opened=fields.Boolean()
    Patient_id=fields.One2many("hms.patient","department_id")