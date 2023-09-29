# Generated by Django 4.2.5 on 2023-09-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stand",
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
                ("localizacao", models.CharField(max_length=150)),
                ("valor", models.FloatField()),
            ],
        ),
    ]