from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from issues.models import Comment, Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description", "place", "severity", "photo"]
        labels = {
            "title": _("Title"),
            "description": _("Description"),
            "place": _("Location"),
            "severity": _("Severity"),
            "photo": _("Photo"),
        }


class IssueCloseForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["status", "date_resolved"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": _(""),
        }
