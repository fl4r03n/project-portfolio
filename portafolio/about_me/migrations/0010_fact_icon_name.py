# Generated by Django 5.0.4 on 2024-09-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_me", "0009_fact_factdesc"),
    ]

    operations = [
        migrations.AddField(
            model_name="fact",
            name="icon_name",
            field=models.CharField(
                blank=True,
                default="bi bi-emoji-smile",
                help_text="Nombre del ícono (ej. bi bi-emoji-smile). Visita https://icons.getbootstrap.com/ para ver la lista completa de íconos.",
                max_length=50,
                null=True,
            ),
        ),
    ]