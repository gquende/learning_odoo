from odoo import fields, models


class SchoolNew(models.Model):
    _name = "school.new"
    name= fields.Char(string="Name")
    