from odoo import fields, models


class MinimalModel(models.Model):
    _inherit = "hr.employee"
    _name = "employee.model"
    shift_id= fields.Many2one("shift.model",string="Shift Schedule")
