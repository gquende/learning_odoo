from odoo import http

class Shift(http.Controller):
    @http.route('/shift/home', auth='public')
    def index(self, **kw):
        return http.request.render('shift_schedule.index',{})