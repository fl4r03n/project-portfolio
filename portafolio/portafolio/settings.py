# settings.py

import os

# Determinar el entorno
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Importar las configuraciones adecuadas según el entorno
if ENVIRONMENT == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *