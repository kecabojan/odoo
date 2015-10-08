# -*- coding: utf-8 -*-

from openerp import models, fields, api

class abcd(models.Model):
    _name = 'abcd.abcd'

    name = fields.Char(string='ABCD Name', required=True)
    description = fields.Text(string='ABCD Description')
    firstname = fields.Char(string='ABCD First Name')


class Partner(models.Model):
    """
    Extends res.partner model and adds new fields.
    """

    _name = 'res.partner'  # comment out because we want to extend the features or res.partner
    _inherit = 'res.partner'

    firstname = fields.Char(string='First name')    # new field

