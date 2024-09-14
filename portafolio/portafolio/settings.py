# settings.py

from decouple import config

# Determinar el entorno
ENVIRONMENT = config("ENVIRONMENT")

# Importar las configuraciones adecuadas según el entorno
if ENVIRONMENT == 'prod':
    from .settings_prod import *
else:
    from .settings_dev import *