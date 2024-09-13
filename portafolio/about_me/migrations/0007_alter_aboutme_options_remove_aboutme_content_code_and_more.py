# Generated by Django 5.0.4 on 2024-09-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_me", "0006_portfolioheader_alter_knowledge_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aboutme",
            options={"verbose_name": "Sobre mí", "verbose_name_plural": "Sobre mí"},
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="content_code",
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="education",
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="experience",
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="image",
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="link",
        ),
        migrations.RemoveField(
            model_name="aboutme",
            name="skills",
        ),
        migrations.AddField(
            model_name="aboutme",
            name="age",
            field=models.IntegerField(default=21, verbose_name="Edad"),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="birthday",
            field=models.CharField(
                default="1 May 1995", max_length=100, verbose_name="Cumpleaños"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="city",
            field=models.CharField(
                default="New York, USA", max_length=100, verbose_name="Ciudad"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="degree",
            field=models.CharField(
                default="Master", max_length=50, verbose_name="Grado"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="desc_long",
            field=models.TextField(
                default="Officiis eligendi itaque...", verbose_name="Descripción Larga"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="desc_short",
            field=models.TextField(
                default="Lorem ipsum dolor sit amet...",
                verbose_name="Descripción Corta",
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="email",
            field=models.EmailField(
                default="email@example.com", max_length=254, verbose_name="Email"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="freelance",
            field=models.CharField(
                default="Available", max_length=50, verbose_name="Freelance"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="name",
            field=models.CharField(
                default="Developer, Video Editor", max_length=100, verbose_name="Nombre"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="phone",
            field=models.CharField(
                default="+123 456 7890", max_length=20, verbose_name="Teléfono"
            ),
        ),
        migrations.AddField(
            model_name="aboutme",
            name="website",
            field=models.URLField(default="www.example.com", verbose_name="Sitio Web"),
        ),
    ]