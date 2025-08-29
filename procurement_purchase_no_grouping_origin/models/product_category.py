from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = "product.category"

    procured_purchase_grouping = fields.Selection(
        selection_add=[
            ("origin", "Group by Origin"),
        ],
        ondelete={"origin": "set default"},
    )