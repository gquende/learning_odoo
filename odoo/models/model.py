from odoo import models, fields


class MinimalModel(models.Model):
    _name = 'test.model'

    name = fields.Char('name')
    age = fields.Integer('age')
