from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # Valida las imagenes de todos los modulos 5 MB
    if image.size > max_size:
        raise ValidationError("El tamaño de la imagen no debe exceder los 5 MB.")