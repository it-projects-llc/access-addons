def migrate(cr, installed_version):
    cr.execute("UPDATE res_users SET is_readonly = NOT is_regular_user")
