# -*- coding: utf-8 -*-

from odoo import models, fields, api

#class test171220_product(models.Model):
#    _inherit = 'product.template'
#   stocking_item = fields.Boolean("Stocking Item")

#class test171220_stock(models.Model):
#    _inherit = 'stock.move'
#    description = fields.Text("Description", related='product_id.description_picking', store=True)
	
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100