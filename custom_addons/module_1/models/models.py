# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class module_1(models.Model):
    _name = 'module_1.module_1'
    _description = 'module_1.module_1'

    name = fields.Char()
    value = fields.Integer()
    dob = fields.Date(string="Date of birdth", default=datetime.today())
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.constrains('name', 'value2', 'value')
    def _check_name(self):
        for rec in self:
            if len(rec.name) > 10:
                raise ValidationError("length of name is less than 10.")
            if rec.value > 100:
                raise ValidationError("Value is less than 100")
            if rec.value2 != float(rec.value) / 100:
                raise ValidationError("Value 2 is not valid")
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.model
    def create(self, vals_list):
        vals_list['name'] = 'VT_' + vals_list['name']
        vals_list['value'] = vals_list['value'] + 1
        return super(module_1, self).create(vals_list)
