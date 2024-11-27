from django.utils import timezone
from django.views.generic import ListView
from django_filters.views import FilterView

from dashboards.filters import IssueFilter
from issues.models import Issue


class ResidentDashboardView(ListView, FilterView):
    template_name = "dashboards/dashboard_resident.html"
    context_object_name = "issues"
    filterset_class = IssueFilter

    def get_queryset(self):
        queryset = Issue.objects.filter(
            building=self.request.user.building,
            status__in=[Issue.IssueStatusChoices.OPEN],
        ).order_by("-date_reported") | Issue.objects.filter(
            building=self.request.user.building,
            status=Issue.IssueStatusChoices.CLOSED,
            date_resolved__gte=timezone.now() - timezone.timedelta(days=14),
        )

        self.filterset = IssueFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
        # return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project2 - Resident"
        context["building_id"] = self.request.user.building.id
        context["form"] = self.filterset.form
        return context
