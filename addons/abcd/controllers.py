# -*- coding: utf-8 -*-
from openerp import http


class Abcd(http.Controller):
    @http.route('/abcd/abcd/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/abcd/abcd/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('abcd.listing', {
            'root': '/abcd/abcd',
            'objects': http.request.env['abcd.abcd'].search([]),
        })

    @http.route('/abcd/abcd/objects/<model("abcd.abcd"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('abcd.object', {
            'object': obj
        })