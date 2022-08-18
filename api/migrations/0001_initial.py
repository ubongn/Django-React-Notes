# Generated by Django 4.1 on 2022-08-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("body", models.TextField(blank=True, max_length=255)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("created", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
