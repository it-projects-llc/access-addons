==================
 Block backend UI
==================

This technical module allows blocking backend access and display the message

In order to do that, dependent module need to override ``ir.http`` 's session_info method and return
dictionary with following keys:

* ``database_block_message`` - the displayed message itself. Can be HTML
* ``database_block_is_warning`` - if true, backend is not blocked, but displayed message is shown as warning (``web_responsive`` must be installed in order for warning to be displayed)

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: it@it-projects.info

Contributors
============

* `Eugene Molotov <https://github.com/em230418>`__:
