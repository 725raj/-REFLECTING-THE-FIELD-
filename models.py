# -*- coding: utf-8 -*-

from odoo import models, fields, api
"""
class task_new(models.Model):
    _name = 'task_new.task_new'
"""

class HR(models.Model):
    _name = 'task_new.task_new'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    department_id = fields.Many2one('hr.department',related='employee_id.department_id',string="Department") 


    @api.onchange('employee_id')
    def _onchange_employee(self):
        self.department_id = self.employee_id.department_id