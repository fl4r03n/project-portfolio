from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Project(models.Model):

    title =  models.CharField(_("Titulo"), max_length=150)
    description = models.TextField(_("Descripcion"), )
    image = models.ImageField(_("Imagen"), upload_to="projects") #a sub carpeta projects la raiz es media
    link = models.URLField(_("URL"), max_length=180, blank=True, null=True)
    created = models.DateTimeField(_("Creado"), auto_now_add=True)
    updated = models.DateTimeField(_("Actualizado"), auto_now=True)
    content_code = models.TextField(_("Codigo a incorporar"),blank=True, null=True)

    class Meta:
        verbose_name = _("proyecto")
        verbose_name_plural = _("proyectos")
        ordering = ["-created"]

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
#        return reverse("_detail", kwargs={"pk": self.pk})