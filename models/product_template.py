from odoo import models, fields, api
import re

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_numeric_part(self, code):
        """Extracts the numeric part from a string."""
        return ''.join(filter(str.isdigit, code))

    def compute_default_code(self):
        """Compute a new default code for the product."""
        largest_code_record = self.env['product.template'].search(
            [], order='default_code desc', limit=1
        )
        largest_code = largest_code_record.default_code
        if largest_code:
            numeric_part = self.get_numeric_part(largest_code)
            try:
                new_code_number = int(numeric_part) + 1 if numeric_part else 1
            except ValueError:
                new_code_number = 1
        else:
            new_code_number = 1
        return str(new_code_number)

    default_code = fields.Char(compute='compute_default_code', store=True, readonly=False)

