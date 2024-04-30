
import os

# Determinar el entorno
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Importar las configuraciones adecuadas según el entorno
if ENVIRONMENT == 'production':
    from .wsgi_prod import *
else:
    from .wsgi_dev import *