from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    is_readonly = fields.Boolean()

    def toggle_readonly(self):
        for user in self:
            user.is_readonly = not user.is_readonly
