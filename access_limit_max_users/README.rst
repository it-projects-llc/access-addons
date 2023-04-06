=======================
 Limit number of users
=======================

With this module you can limit number of users.

This module creates record with external id `access_limit_max_users.max_users_limit`
that defines max amount of users can have current database. By default it is
number of active users at moment of installation of this module.

In order to make user to be ignoring the limit, you can use field ``is_excluded_from_limiting`` in one of the following ways:

* Create or set ``is_excluded_from_limiting`` to True in supersuper (sudo) mode. See `<tests/test_excluded_users.py>`_
* Define user record in `data files <https://www.odoo.com/documentation/14.0/reference/data.html>`__ with ``is_excluded_from_limiting`` set to True.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: it@it-projects.info

Contributors
============

* `Eugene Molotov <https://github.com/em230418>`__:
