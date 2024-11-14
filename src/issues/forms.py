from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from issues.models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description", "place", "severity"]
        labels = {
            "title": _("Title"),
            "description": _("Description"),
            "place": _("Location"),
            "severity": _("Severity"),
        }
