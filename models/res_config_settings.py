# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Match school_core: Boolean + config_parameter + default=False,
    # and persist via get_values/set_values as strings "True"/"False".
    # (set_param deletes the key on Python False; string "False" keeps it.)
    spm_show_poweredby = fields.Boolean(
        string="Show Powered by",
        config_parameter="spm_show_poweredby",
        default=False,
    )
    spm_poweredby_text = fields.Char(
        string="Powered by text",
        config_parameter="spm_poweredby_text",
        default="Powered by Odoo",
    )
    spm_poweredby_url = fields.Char(
        string="Powered by URL",
        config_parameter="spm_poweredby_url",
        default="https://www.odoo.com?utm_source=db&utm_medium=auth",
    )

    spm_show_documentation = fields.Boolean(
        string="Show Documentation",
        config_parameter="spm_show_documentation",
        default=False,
    )
    spm_documentation_text = fields.Char(
        string="Documentation label",
        config_parameter="spm_documentation_text",
        default="Documentation",
    )
    spm_documentation_url = fields.Char(
        string="Documentation URL",
        config_parameter="spm_documentation_url",
        default="https://www.odoo.com/documentation/18.0",
    )

    spm_show_support = fields.Boolean(
        string="Show Support",
        config_parameter="spm_show_support",
        default=False,
    )
    spm_support_text = fields.Char(
        string="Support label",
        config_parameter="spm_support_text",
        default="Support",
    )
    spm_support_url = fields.Char(
        string="Support URL",
        config_parameter="spm_support_url",
        default="https://www.odoo.com/buy",
    )

    spm_show_account = fields.Boolean(
        string="Show My Odoo.com account",
        config_parameter="spm_show_account",
        default=False,
    )
    spm_account_text = fields.Char(
        string="My Account label",
        config_parameter="spm_account_text",
        default="My Odoo.com account",
    )
    spm_account_url = fields.Char(
        string="My Account URL",
        config_parameter="spm_account_url",
        default="https://accounts.odoo.com/my",
    )

    def get_values(self):
        res = super().get_values()
        icp = self.env["ir.config_parameter"].sudo()
        res["spm_show_poweredby"] = (
            icp.get_param("spm_show_poweredby", "False") == "True"
        )
        res["spm_show_documentation"] = (
            icp.get_param("spm_show_documentation", "False") == "True"
        )
        res["spm_show_support"] = (
            icp.get_param("spm_show_support", "False") == "True"
        )
        res["spm_show_account"] = (
            icp.get_param("spm_show_account", "False") == "True"
        )
        return res

    def set_values(self):
        super().set_values()
        icp = self.env["ir.config_parameter"].sudo()
        icp.set_param(
            "spm_show_poweredby",
            "True" if self.spm_show_poweredby else "False",
        )
        icp.set_param(
            "spm_show_documentation",
            "True" if self.spm_show_documentation else "False",
        )
        icp.set_param(
            "spm_show_support",
            "True" if self.spm_show_support else "False",
        )
        icp.set_param(
            "spm_show_account",
            "True" if self.spm_show_account else "False",
        )
