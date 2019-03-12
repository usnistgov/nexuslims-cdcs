""" Menu configuration for mdcs. The following menus are displayed:

  * No dropdown menu

    * Home
    * Data Curation

  * Data Exploration menu

    * Search by Keyword
    * Build a Custom Query

  * Composer menu

    * Create New Template
    * My Template
    * My Types

  * Dashboard menu

    * My Workspaces
    * My Records
    * My Drafts
    * My Files

  * Help menu

    * API Documentation
    * Contact
    * Help
"""

from django.core.urlresolvers import reverse
from mdcs.settings import CURATE_MENU_NAME
from menu import Menu, MenuItem

Menu.add_item(
    "nodropdown", MenuItem("Home", reverse("core_main_app_homepage"), icon="home")
)

Menu.add_item(
    "nodropdown", MenuItem(CURATE_MENU_NAME, reverse("core_curate_index"))
)
Menu.add_item(
    "explorer", MenuItem("Search by Keyword", reverse("core_explore_keyword_app_search"))
)

Menu.add_item(
    "explorer", MenuItem("Build a Custom Query", reverse("core_explore_example_index"))
)

Menu.add_item(
    "composer", MenuItem("Create New Template", reverse("core_composer_build_template", args=("new",)))
)

Menu.add_item(
    "composer", MenuItem("My Template", reverse("core_dashboard_templates"))
)

Menu.add_item(
    "composer", MenuItem("My Types", reverse("core_dashboard_types"))
)

Menu.items["dashboard"] = []
Menu.add_item(
    "dashboard", MenuItem("My Workspaces", reverse('core_dashboard_workspaces'), icon="folder-open")
)

Menu.add_item(
    "dashboard", MenuItem("My Records", reverse('core_dashboard_records'), icon="file-text-o")
)

Menu.add_item(
    "dashboard", MenuItem("My Drafts", reverse('core_dashboard_forms'), icon="file-text-o")
)

Menu.add_item(
    "dashboard", MenuItem("My Files", reverse('core_dashboard_files'), icon="file")
)

Menu.add_item(
    "help", MenuItem("API Documentation", reverse("swagger_view"), icon="cogs")
)

Menu.add_item(
    "help", MenuItem("Contact", reverse("core_website_app_contact"), icon="envelope")
)

Menu.add_item(
    "help", MenuItem("Help", reverse("core_website_app_help"), icon="question-circle")
)