# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Browser tab favicon (same field name as muk_web_theme if installed).
    favicon = fields.Binary(string="Company Favicon", attachment=True)
