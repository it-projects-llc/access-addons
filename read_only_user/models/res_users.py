from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    is_readonly = fields.Boolean()

    def toggle_readonly(self):
        for user in self:
            user.is_readonly = not user.is_readonly

            if user.is_readonly:
                user._hack_init_odoobot()

    def _hack_init_odoobot(self):
        if "mail.channel" not in self.env:
            return

        Channel = self.with_user(self).sudo().env["mail.channel"]

        init_odoobot = getattr(Channel, "init_odoobot", None)
        if not init_odoobot:
            return

        init_odoobot()
