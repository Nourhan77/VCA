
import re

from odoo import models , fields, api
from odoo.exceptions import ValidationError

class HMSPatient (models.Model):
    _name="hms.patient"
    _description="HMS Lab"

    
    First_name=fields.Char(required=True)
    Last_name=fields.Char()
    doctors_ids=fields.Many2many("hms.doctor")
    Birth_date=fields.Date()
    History=fields.Html()
    CR_Ratio =fields.Float()
    Blood_type=fields.Selection([ ('a', 'a'),('b', 'b'),('c', 'c')])
    PCR=fields.Boolean()
    Image=fields.Image()
    Address=fields.Text()
    Age=fields.Integer(compute="calc_age")
    department_id=fields.Many2one("hms.department")
    department_capacity=fields.Integer(related="department_id.department_capacity")
    logs_ids=fields.One2many("hms.patient.log","patient_id")
    state=fields.Selection([ 
        ('UN', 'Undetermined'),
        ('G', 'Good'),
        ('F', 'Fair'),
        ("S","Serious")
        ],defualt="UN")
    description=fields.Char()
    Email=fields.Char()


    def _add_log(self , state):
            self.env["hms.patient.log"].create ( {

                "description": f"State changed to {state}",
                "patient_id":self.id
            })

    def set_good(self):
        self.state='G'
        self._add_log('Good')


    def set_undetermined(self):
        self.state='UN'
        self._add_log('Undetermined')

    def set_fair(self):
        self.state='F'
        self._add_log('Fair')

    def set_serious(self):
        self.state='S'
        self._add_log("Serious")

    
    @api.onchange("Age")

    def _onchange_age(self):
        if self.Age and self.Age < 30:
            self.PCR= True
            return {

                "warning":{

                    "title":"Warning",
                    "message":"PCR field has been checked."
                }
            }

    @api.constrains("email")
    def _validate_email(self):
        reg=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.fullmatch(reg,self.email):
            raise ValidationError ("Email is not valid.")

    


    _sql_constraints=[('unique_email','UNIQUE(email)','Email is already exists')]



'''
    @api.depends("Birth_date")
    def calc_age(self):
        
            if self.Birth_date:
                diff= fields.Date.today() - self.Birth_date
                self.Age= diff.days // 365
'''

class PatientLog(models.Model):
    _name="hms.patient.log"
    description=fields.Text()
    patient_id=fields.Many2one("hms.patient")