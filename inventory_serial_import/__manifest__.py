# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Import Serial Numbers on Delivery Orders',
    'version': '10.0.1.0.0',
    'website': 'http://www.pptssolutions.com',
    'category': 'inventory',
    'depends': ['base', 'stock'],
    'license': 'LGPL-3',
    'support': 'business@pptservices.com',
    'summary': 'Product Serial Numbers Import on Delivery Orders',
    'data': [
        'views/inventory_serial_import_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
