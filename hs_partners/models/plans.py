from odoo import models, fields

class MinimalModel(models.Model):
    _name='partners.link'
    url= fields.Char('url')
    date=fields.Char('date')