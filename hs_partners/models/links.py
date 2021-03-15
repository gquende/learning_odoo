from odoo import models, fields

class MinimalModel(models.Model):
    _name = "partners.model.links"
    url = fields.Char('Url')
