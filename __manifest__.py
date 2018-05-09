# -*- coding: utf-8 -*-
{
    'name': "test171220",

    'summary': """
        Exercise in adding a custom field to inherited model.""",

    'description': """
        
    """,

    'author': "Tony Cook",
    'website': "http://www.precisionepllc.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','mrp','stock','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}