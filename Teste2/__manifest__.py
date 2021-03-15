{
    'name': "Partners",

    'summary': """Manage trainings""",

    'description': """
       Testanto as configuracoes basicas
    """,

    'author': "Geraldo Quende",
    'website': "http://www.geraldoquende.gq",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/model_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
