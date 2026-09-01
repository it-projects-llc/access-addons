from odoo import api, models

from odoo.addons.read_only_user.const import mail_message_exception


class MailChannel(models.Model):
    _inherit = "mail.channel"

    @api.model
    def init_odoobot(self):
        return super(
            MailChannel,
            self.sudo().with_context(mail_message_exception=mail_message_exception),
        ).init_odoobot()
