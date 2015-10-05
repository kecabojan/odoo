# -*- coding: utf-8 -*-
{
    'name': "Partner Extender",

    'summary': """
        Extended partner model and views""",

    'description': """
        Module written as a test
    """,

    'author': "Bojan Keca",
    'website': "https://www.linkedin.com/in/kecabojan",

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
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False
}