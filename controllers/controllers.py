# -*- coding: utf-8 -*-
from odoo import http

# class Test171220(http.Controller):
#     @http.route('/test171220/test171220/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test171220/test171220/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test171220.listing', {
#             'root': '/test171220/test171220',
#             'objects': http.request.env['test171220.test171220'].search([]),
#         })

#     @http.route('/test171220/test171220/objects/<model("test171220.test171220"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test171220.object', {
#             'object': obj
#         })