=====================
 Database Limit Size
=====================

This module allows blocking backend access when database limit is exceeded

On loading backend page, module fetches size of database (including filestore) and compares it with value, that
is defined in "System Parameters" as ``database_limit_size``. Value is expected to be in bytes.

If ``database_limit_size`` is not given or zero, there is no limit.

Roadmap
=======

* Customize percentage of the limit which, if exceeded, would indicate a warning. As for now it is hardcoded to 90%

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: it@it-projects.info

Contributors
============

* `Eugene Molotov <https://github.com/em230418>`__:
