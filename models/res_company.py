# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Browser tab favicon (same field name as muk_web_theme if installed).
    favicon = fields.Binary(string="Company Favicon", attachment=True)

    # Social / link preview (Open Graph + Twitter cards — used by most platforms)
    spm_social_preview_title = fields.Char(
        string="Social Preview Title",
        default="finpal.pk",
        help="Title shown when this site link is shared on social apps.",
    )
    spm_social_preview_logo = fields.Binary(
        string="Social Preview Logo",
        attachment=True,
        help="Image shown when this site link is shared on social apps.",
    )
