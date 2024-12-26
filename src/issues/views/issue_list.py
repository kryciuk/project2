from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
from django.views.generic import ListView

from core.access_controls_utils import redirect_no_permission
from issues.filters import IssuePropertyManagerFilter
from issues.models import Issue


class IssueListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Issue
    template_name = "issues/issue_list.html"
    context_object_name = "issues"
    filterset_class = IssuePropertyManagerFilter
    paginate_by = 5
    extra_context = {"title": "Project2"}
    permission_required = "issues.change_issue"

    def get_queryset(self):
        queryset = Issue.objects.filter(status=Issue.IssueStatusChoices.OPEN) | Issue.objects.filter(
            status=Issue.IssueStatusChoices.CLOSED, date_resolved__gte=timezone.now() - timezone.timedelta(days=14)
        )
        self.filterset = IssuePropertyManagerFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context

    def handle_no_permission(self):
        return redirect_no_permission(self.request)
