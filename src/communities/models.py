import os

import qrcode as qr
from django.contrib.sites.models import Site
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from PIL import Image, ImageDraw

from core import settings

from .consts import CHOICES_CITIES


class Building(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    city = models.CharField(choices=CHOICES_CITIES)
    postal_code = models.CharField(
        max_length=7, null=True, blank=True, validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{3}$")]
    )
    street = models.CharField(max_length=30, null=True, blank=True)
    street_number = models.IntegerField(null=True, blank=True)
    manager = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        limit_choices_to={"groups__name__in": ["Property Manager", "Administrator"]},
        related_name="managed_building",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} ID:{self.pk}"

    def get_absolute_url(self):
        return reverse("building-create")

    def create_issue_report_qr_code(self):
        building_id = self.id
        current_site = Site.objects.get_current()
        url = reverse("issue-report", kwargs={"id_building": building_id})

        qrcode = qr.make(f"{current_site.domain}{url}")
        canvas = Image.new("RGB", (600, 600), "white")
        ImageDraw.Draw(canvas)
        qr_width, qr_height = qrcode.size
        paste_position = ((600 - qr_width) // 2, (600 - qr_height) // 2)
        canvas.paste(qrcode, paste_position)

        file_name = f"building{building_id}_qrcode.png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        canvas.save(file_path)
        canvas.close()
