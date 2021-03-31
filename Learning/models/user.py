from odoo import fields, models


class User(models.Model):

    _name = "user.model"
    _inherit = "res.users"
    name = fields.Char("nome")
    sexo = fields.Char("sexo")


