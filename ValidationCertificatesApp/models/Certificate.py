from odoo import models , fields, api

class Certificate (models.Model):
    _name="vca.cert"
    _description="VCA Certificate"

    vehicle_type=fields.Selection([ ('car', 'Car'),('bus', 'Bus'),('minibus', 'Minibus'),('microbus','Microbus')])
    traffic_departments=fields.Many2one("vca.traffic_dep")
    type=fields.Many2one("vca.cert_types")
    Customer_id=fields.Many2one("vca.customers")
    customer_name=fields.Char(related="Customer_id.name")
    car_model=fields.Date()
    brand=fields.Many2one("vca.brands")
    price=fields.Float()
    Chassis_number=fields.Char()
    motor_number= fields.Char()
    is_printed=fields.Boolean()
    print_ids=fields.One2many("vca.user.print","user_id")
    description=fields.Char()
    serial_number=fields.Char('Order Reference',defult="New")
    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('vca.cert')
        return super(Certificate, self).create(vals)

    def _add_log(self ):
            self.env["vca.user.print"].create ( {
                "description": f"the report printed",
                "user_id":self.id
            })

    def printed(self):
        self.is_printed=True
        self._add_log()


    def print_report(self):
        self.is_printed=True
        return self.env.ref('ValidationCertificatesApp.vca_cert_report_action').report_action(self)
        

    
    def reprint_report (self):
        self.is_printed=False


class User_Print(models.Model):
    _name="vca.user.print"
    description=fields.Text()
    user_id=fields.Many2one("vca.cert")

