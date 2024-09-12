from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from core.models import validate_image_size
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

class Education(models.Model):
    degree = models.CharField(_("Grado"), max_length=100, default="Academia")
    institution = models.CharField(_("Instituto"), max_length=100)
    start_year = models.IntegerField(_("Año inicio"), default=2000)
    end_year = models.IntegerField(_("Año fin"), null=True, blank=True)
    description = models.TextField(_("Descripción"))

    class Meta:
        verbose_name = _("Educacion")
        verbose_name_plural = _("Educaciones")
        ordering = ["start_year"]

    def __str__(self):
        return self.degree


class Experience(models.Model):
    title = models.CharField(_("Titulo"), max_length=100)
    company = models.CharField(_("Compañia"), max_length=100, default="Independiente")
    start_year = models.IntegerField(_("Año inicio"), default=2000)
    end_year = models.IntegerField(
        _("Año fin"), null=True, blank=True
    )  # null=True, blank=True if it's the current job
    description = models.TextField(_("Descripción"))
    responsibilities = models.TextField(
        _("Responsabilidades"), null=True, blank= True
    )  # Store responsibilities as a comma-separated list or use another related model

    class Meta:
        verbose_name = _("Experiencia")
        verbose_name_plural = _("Experiencias")
        ordering = ["start_year"]

    def __str__(self):
        return self.title

class ResumeDesc(models.Model):
    tittle_section = models.CharField(
        _("Título de Sección"), max_length=100, default="Resume"
    )
    desc_section = models.TextField(
        _("Descripción de Sección"), default="Magnam dolores commodi suscipit..."
    )

    def save(self, *args, **kwargs):
        if not self.pk and ResumeDesc.objects.exists():
            raise ValueError("Solo puede existir una instancia de ResumeDesc")
        return super(ResumeDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Currículum")
        verbose_name_plural = _("Descripciones de Currículum")

    def __str__(self):
        return self.tittle_section

class SkillDesc(models.Model):
    tittle_section = models.CharField(
        _("Título de Sección"), max_length=100, default="Skills"
    )
    desc_section = models.TextField(
        _("Descripción de Sección"), default="Magnam dolores commodi suscipit..."
    )

    def save(self, *args, **kwargs):
        if not self.pk and SkillDesc.objects.exists():
            raise ValueError("Solo puede existir una instancia de SkillDesc")
        return super(SkillDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Habilidades")
        verbose_name_plural = _("Descripciones de Habilidades")

    def __str__(self):
        return self.tittle_section

class Skill(models.Model):
    HARD = 'hard'
    SOFT = 'soft'
    SKILL_TYPE_CHOICES = [
        (HARD, 'Hard Skill'),
        (SOFT, 'Soft Skill'),
    ]

    name = models.CharField(_("Nombre Habilidad"), max_length=100)
    percentage = models.IntegerField(_("Porcentaje"), null=True, blank=True)  # Opcional para soft skills
    image = models.ImageField(_("Imagen"), upload_to="skill_icons", null=True, blank=True, validators=[validate_image_size])
    skill_type = models.CharField(_("Tipo de Habilidad"), max_length=4, choices=SKILL_TYPE_CHOICES, default="soft")

    class Meta:
        verbose_name = _("Habilidad")
        verbose_name_plural = _("Habilidades")
        ordering = ["-pk"]

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Skill)
def delete_old_image_skill(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Skill.objects.get(pk=instance.pk)
        except Skill.DoesNotExist:
            return
        if old_instance.image and old_instance.image != instance.image:
            if os.path.isfile(old_instance.image.path):
                os.remove(old_instance.image.path)

@receiver(pre_delete, sender=Skill)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

class AboutMe(models.Model):
    title = models.CharField(_("Título"), max_length=100)
    name = models.CharField(
        _("Nombre"),
        max_length=100,
        default="Developer, Video Editor",
    )
    desc_short = models.TextField(
        _("Descripción Corta"), default="Lorem ipsum dolor sit amet..."
    )
    birthday = models.CharField(_("Cumpleaños"), max_length=100, default="1 May 1995")
    website = models.URLField(_("Sitio Web"), max_length=200, default="www.example.com")
    phone = models.CharField(_("Teléfono"), max_length=20, default="+123 456 7890")
    city = models.CharField(_("Ciudad"), max_length=100, default="New York, USA")
    age = models.IntegerField(_("Edad"), default=21)
    degree = models.CharField(_("Grado"), max_length=50, default="Master")
    email = models.EmailField(_("Email"), default="email@example.com")
    freelance = models.CharField(_("Freelance"), max_length=50, default="Available")
    desc_long = models.TextField(
        _("Descripción Larga"), default="Officiis eligendi itaque..."
    )
    created = models.DateTimeField(_("Creado"), auto_now_add=True)
    updated = models.DateTimeField(_("Actualizado"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValueError("Solo puede existir una instancia de AboutMe")
        return super(AboutMe, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Sobre mí")
        verbose_name_plural = _("Sobre mí")

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
            
class FactDesc(models.Model):
    tittle_section = models.CharField(
        _("Título de Sección"), max_length=100, default="Facts"
    )
    desc_section = models.TextField(
        _("Descripción de Sección"), default="Magnam dolores commodi suscipit..."
    )

    def save(self, *args, **kwargs):
        if not self.pk and FactDesc.objects.exists():
            raise ValueError("Solo puede existir una instancia de FactDesc")
        return super(FactDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Datos")
        verbose_name_plural = _("Descripciones de Datos")

    def __str__(self):
        return self.tittle_section


class Fact(models.Model):
    title = models.CharField(_("Título del Dato"), max_length=100)
    end_value = models.IntegerField(_("Valor Final"), default=0)
    duration = models.IntegerField(_("Duración"), default=1)
    icon_name = models.CharField(
        max_length=50,
        default="bi bi-emoji-smile",
        help_text=(
            "Nombre del ícono (ej. bi bi-emoji-smile). "
            "Visita https://icons.getbootstrap.com/ para ver la lista completa de íconos."
        ), blank = True, null= True
    )

    class Meta:
        verbose_name = _("Dato")
        verbose_name_plural = _("Datos")

    def __str__(self):
        return self.title