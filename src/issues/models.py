from django.db import models
from django.urls import reverse
from django.utils import timezone

from communities.models import Building
from users.models import CustomUser


class Issue(models.Model):
    class IssuePlaceChoices(models.TextChoices):
        COMMON_AREA = "Część wspólna"
        APARTMENT = "Mieszkanie"
        GARAGE = "Garaż"

    class IssueSeverityChoices(models.TextChoices):
        LOW = "Niska"
        MEDIUM = "Średnia"
        HIGH = "Wysoka"

    class IssueStatusChoices(models.TextChoices):
        OPEN = "Otwarta"
        IN_PROGRESS = "W trakcie"
        RESOLVED = "Rozwiązana"
        CLOSED = "Zamknięta"

    title = models.CharField(max_length=30)
    description = models.TextField()
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)
    place = models.CharField(choices=IssuePlaceChoices.choices)
    severity = models.CharField(choices=IssueSeverityChoices.choices)
    status = models.CharField(choices=IssueStatusChoices.choices)
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
