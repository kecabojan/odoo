# -*- coding: utf-8 -*-
{
    'name': "ABCD",

    'summary': """
        Simple ABCD module""",

    'description': 'Written as a job test',

    'author': "Bojan Keca",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'demo.xml',
        'views/abcd_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}