from odoo import http

class Shift(http.Controller):

    @http.route('/shift/home', auth='public', website=True)
    def index(self, **kw):
        #return http.request.render('shift_schedule.index',{})
        shifts = http.request.env['shift.model']
        userData=shifts.search([]);
        lista=[]
        for user in userData:
            user.start_time=user.start_time[10:16]
            user.stop_time=user.stop_time[10:16]
            lista.append(user)

        return http.request.render('shift_schedule.index', {'shifts': lista})

    @http.route('/shift', auth='public', website=True)
    def index2(self, **kw):
        shifts = http.request.env['shift.model']
        return http.request.render('shift_schedule.index2', {'shifts': shifts.search([])})

