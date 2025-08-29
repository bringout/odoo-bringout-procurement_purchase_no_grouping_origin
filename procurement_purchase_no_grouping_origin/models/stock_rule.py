
from odoo import models

class StockRule(models.Model):
    _inherit = "stock.rule"

    def _run_buy(self, procurements):
        for procurement, _rule in procurements:
            procurement.values["grouping"] = (
                procurement.product_id.categ_id.procured_purchase_grouping
                or self.env.company.procured_purchase_grouping
            )
        return super()._run_buy(procurements)

    def _make_po_get_domain(self, company_id, values, partner):
        domain = super()._make_po_get_domain(company_id, values, partner)
        if values.get("grouping") == "origin":
            # values["group_id"]["name"] = 'WH/MO/00011'
            domain += (("origin", "=", values["group_id"]["name"]),)

        return domain
