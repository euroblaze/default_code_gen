# Auto Generate Default Code

This Odoo module automatically generates a new default code for each product created in Odoo. The new default code is based on the largest existing default code, incrementing it by 1. 
If the largest existing code contains non-numeric characters, they are stripped out, and only the numeric part is considered for incrementing.

## Features

- Auto-generates a new default code for new products.
- Handles non-numeric


## Deployment and Use

- Place the entire module directory in your Odoo addons path.
- Update the module list in the Odoo interface.
- Install the module through the Odoo Apps interface.

Once installed, the module will automatically generate a `default_code` for each new product created. The code will be displayed in the form view and is set as read-only to prevent manual edits.

This solution adheres to the constraints of avoiding manual steps like copying and pasting or using forbidden opcodes in Automated Actions. It should work seamlessly on the Odoo community edition.

