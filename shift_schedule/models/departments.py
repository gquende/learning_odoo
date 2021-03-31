from odoo import models, fields


class MinimalModel(models.Model):
    _name = "department.model"
    name = fields.Char('name')
    funcionario=fields.Char('funcionario')

