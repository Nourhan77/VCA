
from odoo import models , fields, api

class SequenceOrder (models.Model):
    _name="sequence.order"
    _description="Sequence Order"

    sequence=fields.Char('Order Reference',defult="New")
    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sequence.order')
        return super(SequenceOrder, self).create(vals)