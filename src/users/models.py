from django.contrib.auth.models import AbstractUser
from django.db import models
from invitations.models import Invitation

from communities.models import Building


class CustomUser(AbstractUser):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True, related_name="residents")


class CustomInvitation(Invitation):
    class GroupChoices(models.TextChoices):
        GROUP__PROPERTY_MANAGER = "Property Manager"
        GROUP__RESIDENT = "Resident"
        GROUP__ADMINISTRATOR = "Administrator"

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    group = models.CharField(choices=GroupChoices.choices)
