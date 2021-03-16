from odoo import  models, fields

class MinimalModel(models.Model):
    _name='partners.plans.model'
    name= fields.Char('name')