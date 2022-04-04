# -*- coding: utf-8 -*-
# from odoo import http


# class ArHr(http.Controller):
#     @http.route('/ar_hr/ar_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ar_hr/ar_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ar_hr.listing', {
#             'root': '/ar_hr/ar_hr',
#             'objects': http.request.env['ar_hr.ar_hr'].search([]),
#         })

#     @http.route('/ar_hr/ar_hr/objects/<model("ar_hr.ar_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ar_hr.object', {
#             'object': obj
#         })
