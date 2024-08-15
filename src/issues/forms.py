from django.forms import ModelForm

from issues.models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description", "place", "severity"]
