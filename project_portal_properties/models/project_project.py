# Copyright 2025 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models

from odoo.addons.web_portal_properties.fields import PortalPropertiesDefinition


class ProjectProject(models.Model):
    _inherit = "project.project"

    task_properties_definition = PortalPropertiesDefinition()
