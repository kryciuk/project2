import django_filters
from django.utils.translation import gettext_lazy as _

from communities.models import Building
from issues.models import Issue


class IssuePropertyManagerFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="iexact", label=_("Title"))
    status = django_filters.ChoiceFilter(
        field_name="status", choices=Issue.IssueStatusChoices.choices, label=_("Status")
    )
    severity = django_filters.ChoiceFilter(
        field_name="severity", choices=Issue.IssueSeverityChoices.choices, label=_("Severity")
    )
    building = django_filters.ModelChoiceFilter(queryset=Building.objects.all(), label=_("Building"))

    class Meta:
        model = Issue
        fields = ["title", "status", "severity", "building"]
