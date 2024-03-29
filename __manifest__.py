{
    'name': 'Auto Generate Default Code',
    'version': '1.0',
    'summary': 'Automatically generates default codes for new products',
    'description': 'This module automatically generates a new default code for each product created in Odoo, based on the largest existing code.',
    'author': 'Ashant Chalasani',
    'website': 'https://poweron.software',
    'category': 'Product',
    'depends': ['product','base_automation'],
    'data': [
        'data/auto_default_code_increase.xml',
        'views/product_template_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}

