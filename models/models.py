# -*- coding: utf-8 -*-

from odoo import models, fields, api

class qnote(models.Model):
    _name = 'q_note'

    name = fields.Char()
    date_create = fields.Datetime('Erstelldatum', default=fields.Datetime.now, readonly="true")
    created_by = fields.Many2one('res.users', string="Erstellt durch", default=lambda self: self.env.user, readonly="true")
    date_accepted = fields.Datetime('Bestätigt am:', readonly="true")
    accepted_by = fields.Many2one('res.users', string="Bestätigt durch", readonly="true")
    state = fields.selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ])
    
    description = fields.Html('Beschreibung')
    analysis = fields.Html('Problemanalyse')

    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100