# -*- coding: utf-8 -*-

from odoo import models
from odoo.http import request


def _param_bool(icp, key, default="False"):
    return icp.get_param(key, default) == "True"


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super().session_info()
        try:
            icp = request.env["ir.config_parameter"].sudo()
        except Exception:
            icp = self.env["ir.config_parameter"].sudo()

        result["spm_show_documentation"] = _param_bool(icp, "spm_show_documentation")
        result["spm_documentation_text"] = icp.get_param("spm_documentation_text", "Documentation")
        result["spm_documentation_url"] = icp.get_param(
            "spm_documentation_url", "https://www.odoo.com/documentation/18.0"
        )

        result["spm_show_support"] = _param_bool(icp, "spm_show_support")
        result["spm_support_text"] = icp.get_param("spm_support_text", "Support")
        result["spm_support_url"] = icp.get_param("spm_support_url", "https://www.odoo.com/buy")

        result["spm_show_account"] = _param_bool(icp, "spm_show_account")
        result["spm_account_text"] = icp.get_param("spm_account_text", "My Odoo.com account")
        result["spm_account_url"] = icp.get_param("spm_account_url", "https://accounts.odoo.com/my")

        return result
