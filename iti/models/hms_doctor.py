from odoo import models , fields

class HMSDoctor (models.Model):
    _name="hms.doctor"
    _description="HMS Doctors"
    

    First_name=fields.Char(required=True)
    Last_name=fields.Char(required=True)
    Image=fields.Image()
    full_name=fields.Char(compute="get_full_name")


    def get_full_name(self):
        for rec in self:
            rec.full_name= f"{rec.First_name} {rec.Last_name}"