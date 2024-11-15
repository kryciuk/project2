# Generated by Django 5.1 on 2024-11-14 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("communities", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="building",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"groups__name__in": ["Property Manager", "Administrator"]},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="managed_building",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]