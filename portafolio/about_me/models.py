from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from core.models import validate_image_size
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

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
    
class PortfolioHeader(models.Model):
    name = models.CharField(_("Nombre"), max_length=100, default="Gad Flareon")
    profile_image = models.ImageField(_("Imagen Perfil"), upload_to="profile_images/", blank=True, null=True, validators=[validate_image_size])
    hero_background = models.ImageField(_("Imagen Fondo"), upload_to="hero_backgrounds/", blank=True, null=True, validators=[validate_image_size])
    bio = models.TextField(_("Bio"), blank=True, null=True, help_text="A brief bio or tagline")
    typed_items = models.CharField(_("Lista Items"), max_length=200, help_text="Comma-separated list of items for the typed effect")

    # Social Media Links
    twitter = models.URLField(_("Twitter"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    facebook = models.URLField(_("Facebook"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    instagram = models.URLField(_("Instagram"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    linkedin = models.URLField(_("Linkedin"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    github = models.URLField(_("Github"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    youtube = models.URLField(_("Youtube"), max_length=200, blank=True, null=True, validators=[URLValidator()])
    others = models.URLField(_("Otros"), max_length=200, blank=True, null=True, validators=[URLValidator()])

    def save(self, *args, **kwargs):
        if not self.pk and PortfolioHeader.objects.exists():
            raise ValueError("Solo puede existir una instancia de PortfolioHeader")
        return super(PortfolioHeader, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("PortfolioHeader")
        verbose_name_plural = _("PortfolioHeader")

    def __str__(self):
        return self.name


@receiver(pre_save, sender=PortfolioHeader)
def delete_old_imagen_PortfolioHeader(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = PortfolioHeader.objects.get(pk=instance.pk)
        except PortfolioHeader.DoesNotExist:
            return
        if old_instance.profile_image and old_instance.profile_image != instance.profile_image:
            if os.path.isfile(old_instance.profile_image.path):
                os.remove(old_instance.profile_image.path)
                
        if old_instance.hero_background and old_instance.hero_background != instance.hero_background:
            if os.path.isfile(old_instance.hero_background.path):
                os.remove(old_instance.hero_background.path)


@receiver(pre_delete, sender=PortfolioHeader)
def delete_image_file(sender, instance, **kwargs):
    if instance.profile_image:
        if os.path.isfile(instance.profile_image.path):
            os.remove(instance.profile_image.path)
            
    if instance.hero_background:
        if os.path.isfile(instance.hero_background.path):
            os.remove(instance.hero_background.path)