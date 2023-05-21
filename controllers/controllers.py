# -*- coding: utf-8 -*-
from openerp import http

# class GestionPfe(http.Controller):
#     @http.route('/gestion__pfe/gestion__pfe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion__pfe/gestion__pfe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion__pfe.listing', {
#             'root': '/gestion__pfe/gestion__pfe',
#             'objects': http.request.env['gestion__pfe.gestion__pfe'].search([]),
#         })

#     @http.route('/gestion__pfe/gestion__pfe/objects/<model("gestion__pfe.gestion__pfe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion__pfe.object', {
#             'object': obj
#         })