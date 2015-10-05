# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
import re


class Partner(models.Model):
    """
    Extends res.partner model and adds new fields (first_name and birth_date).
    """
    _inherit = 'res.partner'

    first_name = fields.Char(string='First name')    # new field
    birth_date = fields.Date(string='Birth date')

    @api.multi
    @api.depends('first_name', 'is_company', 'name')
    def _display_name_compute(self):
        # set display_name on all records
        for record in self:
            if not record.is_company:       # private person
                record.display_name = record.name + ' ' + record.first_name
            else:
                record.display_name = record.name

    # override display_name field and use function to compute it.
    # display_name is used in tree, kanban and search views (of base.partner)
    display_name = fields.Char(string='Name', compute=_display_name_compute)     # computed field

    #@api.one
    @api.constrains('email')
    def _email_check(self):
        """
        Use regex to check email address
        """
        pattern = '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$'    # address has to be in form something@something.domain
        if not re.search(pattern, self.email, re.IGNORECASE):
            raise ValidationError("Wrong Email address!")
