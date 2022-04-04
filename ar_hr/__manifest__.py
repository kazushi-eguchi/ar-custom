# -*- coding: utf-8 -*-
{
    'name': "ar_hr",

    'summary': """
        Customize employee information for AR""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kazushi Eguchi in Enzantrades Inc,",
    'website': "http://www.enzantrades.co.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_employee.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
