{
    "name": "Social Preview Modifier",
    "version": "1.1.0",
    "category": "Website",
    "depends": ["web", "base_setup"],
    "data": [
        "data/ir_config_parameter_data.xml",
        "views/modify_login_layout.xml",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "odoo_social_preview_modifier/static/src/js/user_menu.js",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
