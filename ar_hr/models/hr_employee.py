# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ar_hr(models.Model):
    _inherit = 'hr.employee'
    #基本情報
    hr_id = fields.Char('employee code')
    slack_id =fields.Char('Slack ID')
    #desknets
    dn_id = fields.Char('Desknets ID')
    dn_del_flag = fields.Boolean('Delete Flag')
    dn_admin = fields.Boolean('admin')
    #king of time
    kt_id = fields.Char('King of TIme ID')
#     _description = 'ar_hr.ar_hr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
