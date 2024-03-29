# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

{
    "name": """Limit number of users""",
    "summary": """With this module you can limit number of users""",
    "category": "Hidden",
    "images": [],
    "version": "15.0.1.1.1",
    "application": False,
    "author": "IT-Projects LLC, Eugene Molotov",
    "support": "it@it-projects.info",
    "website": "https://github.com/it-projects-llc/access-addons",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["access_limit_records_number"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["data/base_limit_records_number.xml"],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
