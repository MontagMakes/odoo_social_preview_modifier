/** @odoo-module **/

import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { session } from "@web/session";

const userMenuRegistry = registry.category("user_menuitems");

function documentationItem(env) {
    const url = session.spm_documentation_url || "https://www.odoo.com/documentation/18.0";
    const label = session.spm_documentation_text || "Documentation";
    return {
        type: "item",
        id: "documentation",
        description: label,
        href: url,
        callback: () => {
            browser.open(url, "_blank");
        },
        sequence: 10,
    };
}

function supportItem(env) {
    const url = session.spm_support_url || "https://www.odoo.com/buy";
    const label = session.spm_support_text || "Support";
    return {
        type: "item",
        id: "support",
        description: label,
        href: url,
        callback: () => {
            browser.open(url, "_blank");
        },
        sequence: 20,
    };
}

function odooAccountItem(env) {
    const url = session.spm_account_url || "https://accounts.odoo.com/my";
    const label = session.spm_account_text || "My Odoo.com account";
    return {
        type: "item",
        id: "account",
        description: label,
        href: url,
        callback: () => {
            browser.open(url, "_blank");
        },
        sequence: 60,
    };
}

function safeRemove(key) {
    try {
        if (userMenuRegistry.contains(key)) {
            userMenuRegistry.remove(key);
        }
    } catch (_err) {
        // ignore missing keys
    }
}

if (session.spm_show_documentation === false || session.spm_show_documentation === "False") {
    safeRemove("documentation");
} else {
    userMenuRegistry.add("documentation", documentationItem, { force: true });
}

if (session.spm_show_support === false || session.spm_show_support === "False") {
    safeRemove("support");
} else {
    userMenuRegistry.add("support", supportItem, { force: true });
}

if (session.spm_show_account === false || session.spm_show_account === "False") {
    safeRemove("odoo_account");
} else {
    userMenuRegistry.add("odoo_account", odooAccountItem, { force: true });
}
