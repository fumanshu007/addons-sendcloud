# Copyright 2020 Onestein (<https://www.onestein.eu>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SendCloudWebsiteBrandWizard(models.TransientModel):
    _name = "sendcloud.website.brand.wizard"
    _description = "SendCloud Website Brand Wizard"

    def _default_website_ids(self):
        websites = self.env["website"].search(
            [("company_id", "=", self.env.company.id)]
        )
        lines_vals = [
            {
                "website_id": website.id,
                "sendcloud_brand_id": website.sendcloud_brand_id.id,
            }
            for website in websites
        ]
        return self.env["sendcloud.change.website.brand.wizard"].create(lines_vals)

    website_ids = fields.One2many(
        "sendcloud.change.website.brand.wizard",
        "wizard_id",
        string="Websites",
        default=_default_website_ids,
    )

    def button_update(self):
        self.ensure_one()
        for line in self.website_ids:
            website = line.website_id
            website.sendcloud_brand_id = line.sendcloud_brand_id

        company = self.env.company
        company.set_onboarding_step_done("sendcloud_onboarding_website_brand_state")


class SendCloudChangeWebsiteBrandWizard(models.TransientModel):
    _name = "sendcloud.change.website.brand.wizard"
    _description = "Website, Change Brand Wizard"

    wizard_id = fields.Many2one("sendcloud.website.brand.wizard", ondelete="cascade")
    website_id = fields.Many2one(
        "website", required=True, readonly=True, ondelete="cascade"
    )
    sendcloud_brand_id = fields.Many2one(
        "sendcloud.brand",
        compute="_compute_sendcloud_brand_id",
        readonly=False,
        store=True,
    )

    @api.depends("website_id.sendcloud_brand_id")
    def _compute_sendcloud_brand_id(self):
        for record in self:
            record.sendcloud_brand_id = record.website_id.sendcloud_brand_id
