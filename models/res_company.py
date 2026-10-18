# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Browser tab favicon (same field name as muk_web_theme if installed).
    favicon = fields.Binary(string="Company Favicon", attachment=True)

    spm_favicon_token = fields.Char(
        string="Favicon Cache Token",
        compute="_compute_spm_favicon_token",
        help="Changes whenever the favicon image changes. Appended to the favicon "
             "URL so browsers do not serve a stale cached icon.",
    )

    @api.depends("favicon")
    def _compute_spm_favicon_token(self):
        """Token appended to the favicon URL so a new icon shows on the next load.

        Odoo stores ``attachment=True`` Binary fields in ir.attachment together with
        a content checksum, which ir.binary also uses as the HTTP etag (see
        ``ir.binary._record_to_stream``). That checksum changes only when the image
        bytes change, unlike ``write_date``, which changes on every company write.
        """
        attachments = self.env["ir.attachment"].sudo().search(
            [
                ("res_model", "=", "res.company"),
                ("res_field", "=", "favicon"),
                ("res_id", "in", self.ids),
            ]
        )
        tokens = {att.res_id: att.checksum for att in attachments}
        for company in self:
            company.spm_favicon_token = tokens.get(company.id) or ""

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
