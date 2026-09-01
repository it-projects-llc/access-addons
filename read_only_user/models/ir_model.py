from odoo import _, api, models, tools
from odoo.exceptions import AccessError

from ..const import mail_message_exception


class IrModelAccess(models.Model):
    _inherit = "ir.model.access"

    @api.model
    @tools.ormcache_context(
        "self.env.uid",
        "self.env.su",
        "model",
        "mode",
        "raise_exception",
        keys=("lang",),
    )
    def check(self, model, mode="read", raise_exception=True):
        if (
            mode == "create"
            and model == "mail.message"
            and not self.env.context.get("mail_message_exception")
            == mail_message_exception
        ):
            if self._is_readonly_user():
                if raise_exception:
                    raise AccessError(_("Sorry, you are read-only user."))
                else:
                    return False

        if self.env.su:
            return True

        assert isinstance(model, str), "Not a model name: %s" % (model,)  # noqa: UP031

        if mode != "read" and model != "res.users.log":
            if self._is_readonly_user():
                if raise_exception:
                    raise AccessError(_("Sorry, you are read-only user."))
                else:
                    return False

        return super().check(model, mode, raise_exception)

    @tools.ormcache("self.env.uid")
    def _is_readonly_user(self):
        self.env.cr.execute(
            """
SELECT is_readonly
FROM res_users
WHERE id = %s""",
            (self.env.uid,),
        )
        return self.env.cr.fetchone()[0]
