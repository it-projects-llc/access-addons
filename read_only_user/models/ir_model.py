from odoo import _, api, models, tools
from odoo.exceptions import AccessError


class IrModelAccess(models.Model):
    _inherit = "ir.model.access"

    @api.model
    def check(self, model, mode="read", raise_exception=True):
        if self.env.su:
            # User root have all accesses
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
