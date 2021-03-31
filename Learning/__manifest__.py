{
    'name': "Learning Odoo",

    'summary': """This a shift manager created for any company""",

    'description': """
       Shift Manager is a software that provide more function 
    """,

    'author': "Geraldo Quende",
    'website': "http://www.geraldoquende.gq",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly

    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/home.xml',

    ],


    # only loaded in demonstration mode

    'demo': [
        #'demo.xml',
            ],
}
