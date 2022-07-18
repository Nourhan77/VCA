
from odoo.exceptions  import ValidationError
from odoo import models , fields , api
class ResPartner (models.Model): 
    _inherit="res.partner"
    related_customer_id= fields.Many2one("vca.customers")
            

    def unlink (self):
        for rec in self:
            if rec.related_customer_id:
                raise ValidationError ("Can't delete")
            
        return super().unlink()    
            
    