from django.views.generic import ListView

from issues.models import Issue


class ResidentDashboardView(ListView):
    template_name = "dashboards/dashboard_resident.html"
    context_object_name = "issues"

    def get_queryset(self):
        queryset = Issue.objects.filter(
            building=self.request.user.building,
            status__in=[Issue.IssueStatusChoices.OPEN, Issue.IssueStatusChoices.IN_PROGRESS],
        ).order_by("-date_reported")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project2 - Resident"
        return context
