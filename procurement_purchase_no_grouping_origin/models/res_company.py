from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    procured_purchase_grouping = fields.Selection(
        selection_add=[
            ("origin", "Group by Origin"),
        ],
        ondelete={"origin": "set default"},
    )