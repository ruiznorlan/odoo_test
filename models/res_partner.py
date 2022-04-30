from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    last_name = fields.Char(index=True, tracking=True)

    @api.depends('is_company', 'name', 'parent_id.display_name', 'type', 'company_name', 'last_name')
    def _compute_display_name(self):
        diff = dict(show_address=None, show_address_only=None, show_email=None, html_format=None, show_vat=None)
        names = dict(self.with_context(**diff).name_get())
        for partner in self:
            display = names.get(partner.id) if not partner.last_name else names.get(partner.id) + ' ' + partner.last_name
            partner.display_name = display
