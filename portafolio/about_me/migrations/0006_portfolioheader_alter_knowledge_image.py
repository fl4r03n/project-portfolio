# Generated by Django 5.0.4 on 2024-09-11 20:03

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_me", "0005_alter_aboutme_options_alter_knowledge_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioHeader",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="Gad Flareon", max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_images/",
                        validators=[core.models.validate_image_size],
                        verbose_name="Imagen Perfil",
                    ),
                ),
                (
                    "hero_background",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="hero_backgrounds/",
                        validators=[core.models.validate_image_size],
                        verbose_name="Imagen Fondo",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        help_text="A brief bio or tagline",
                        null=True,
                        verbose_name="Bio",
                    ),
                ),
                (
                    "typed_items",
                    models.CharField(
                        help_text="Comma-separated list of items for the typed effect",
                        max_length=200,
                        verbose_name="Lista Items",
                    ),
                ),
                (
                    "twitter",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Twitter",
                    ),
                ),
                (
                    "facebook",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Facebook",
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Instagram",
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Linkedin",
                    ),
                ),
                (
                    "github",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Github",
                    ),
                ),
                (
                    "youtube",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Youtube",
                    ),
                ),
                (
                    "others",
                    models.URLField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Otros",
                    ),
                ),
            ],
            options={
                "verbose_name": "PortfolioHeader",
                "verbose_name_plural": "PortfolioHeader",
            },
        ),
        migrations.AlterField(
            model_name="knowledge",
            name="image",
            field=models.ImageField(upload_to="knowledge_icons", verbose_name="Imagen"),
        ),
    ]