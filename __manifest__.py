# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Procell 2 Step SO Approval',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Adds a 2 step approval process to the sale order confirmation.
        """,
    'depends': ['base','sale'],
    'data': [
        'data/ir_model_fields.xml',
        'data/ir_actions_server.xml',
        'data/ir_ui_views.xml',
        'data/base_automation.xml',
    ],
    'installable': True,
}
