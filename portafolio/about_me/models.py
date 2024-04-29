from django.db import models
from django.utils.translation import gettext_lazy as _

class Education(models.Model):
    institution = models.CharField(_("Institución"), max_length=100)
    description = models.TextField(_("Descripción"))

    class Meta:
        verbose_name = _("Formación")
        verbose_name_plural = _("Formaciones")

    def __str__(self):
        return self.institution

class Experience(models.Model):
    title = models.CharField(_("Título"), max_length=100)
    description = models.TextField(_("Descripción"))

    class Meta:
        verbose_name = _("Experiencia")
        verbose_name_plural = _("Experiencias")

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(_("Habilidad"), max_length=100)
    description = models.TextField(_("Descripción"))

    class Meta:
        verbose_name = _("Habilidad")
        verbose_name_plural = _("Habilidades")

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    title = models.CharField(_("Título"), max_length=100)
    description = models.TextField(_("Descripción"))
    education = models.ForeignKey(Education, verbose_name=_("Formación"), on_delete=models.CASCADE,blank=True,null=True)
    experience = models.ForeignKey(Experience, verbose_name=_("Experiencia"), on_delete=models.CASCADE,blank=True,null=True)
    skills = models.ForeignKey(Skill, verbose_name=_("Habilidad"), on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(_("Imagen"), upload_to="about_me",blank=True, null=True) #a sub carpeta projects la raiz es media
    link = models.URLField(_("URL"), max_length=180, blank=True, null=True)
    created = models.DateTimeField(_("Creado"), auto_now_add=True)
    updated = models.DateTimeField(_("Actualizado"), auto_now=True)
    content_code = models.TextField(_("Codigo a incorporar"),blank=True, null=True)

    class Meta:
        verbose_name = _("Sobre mí")
        verbose_name_plural = _("Sobre mí")
        ordering = ["-pk"]

    def __str__(self):
        return self.title
    

class Knowledge(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(_("Imagen"), upload_to="knowledge_icons")  # Subir imágenes a la carpeta 'knowledge_icons'

    class Meta:
        verbose_name = _("conocimiento")
        verbose_name_plural = _("conocimientos")
        ordering = ["-pk"]

    def __str__(self):
        return self.title