# Generated by Django 5.0.7 on 2024-08-15 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("communities", "0002_building_manager_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="building",
            old_name="manager_id",
            new_name="manager",
        ),
    ]
