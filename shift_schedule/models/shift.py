from odoo import models, fields


class MinimalModel(models.Model):
    # _inherit = 'calendar.event'
    _name = "shift.model"

    name = fields.Char('name')
    hour = fields.Char('hour')
    period = fields.Datetime('period')
    id = fields.Integer("id")
    start_time = fields.Datetime("start_time")
    stop_time = fields.Datetime("stop_time")
    date = fields.Date("date")
    employee_id = fields.Many2one('hr.employee', string='Employee')
    department_id =fields.Many2one('hr.department', string="Department")

    def attrAutomated(self):
        print('Attrib shift automated')
