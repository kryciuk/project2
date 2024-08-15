from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from .choices import CHOICES_CITIES


class Building(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    city = models.CharField(choices=CHOICES_CITIES)
    postal_code = models.CharField(
        max_length=7, null=True, blank=True, validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{3}$")]
    )
    street = models.CharField(max_length=30, null=True, blank=True)
    street_number = models.IntegerField(null=True, blank=True)

    # manager_id = models.ForeignKey()

    def __str__(self):
        return f"{self.name} ID:{self.pk}"

    def get_absolute_url(self):
        return reverse("building-create")
