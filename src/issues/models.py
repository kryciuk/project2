from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from communities.models import Building
from users.models import CustomUser


class Issue(models.Model):
    class IssuePlaceChoices(models.TextChoices):
        COMMON_AREA = ("Common Area", _("Common Area"))
        APARTMENT = ("Apartment", _("Apartment"))
        GARAGE = ("Garage", _("Garage"))

    class IssueSeverityChoices(models.TextChoices):
        LOW = ("Low", _("Low"))
        MEDIUM = ("Medium", _("Medium"))
        HIGH = ("High", _("High"))

    class IssueStatusChoices(models.TextChoices):
        OPEN = ("Open", _("Open"))
        IN_PROGRESS = ("In progress", _("In progress"))
        RESOLVED = ("Resolved", _("Resolved"))
        CLOSED = ("Closed", _("Closed"))

    title = models.CharField(max_length=30)
    description = models.TextField()
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)
    place = models.CharField(choices=IssuePlaceChoices.choices)
    severity = models.CharField(choices=IssueSeverityChoices.choices)
    status = models.CharField(choices=IssueStatusChoices.choices)
    photo = models.ImageField(upload_to="media/issues", null=True, blank=True)
    reported_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="reported_issues")
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_issues"
    )
    date_reported = models.DateTimeField(default=timezone.now)
    date_resolved = models.DateTimeField(null=True, blank=True)
    update_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("building-create")
