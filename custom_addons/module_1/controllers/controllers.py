# -*- coding: utf-8 -*-
# from odoo import http


# class Module1(http.Controller):
#     @http.route('/module_1/module_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_1/module_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_1.listing', {
#             'root': '/module_1/module_1',
#             'objects': http.request.env['module_1.module_1'].search([]),
#         })

#     @http.route('/module_1/module_1/objects/<model("module_1.module_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_1.object', {
#             'object': obj
#         })
