from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView

from core.access_controls_utils import redirect_no_permission
from issues.forms import IssueCloseForm
from issues.models import Issue


class IssueCloseView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueCloseForm
    template_name = "issues/issue_list.html"
    context_object_name = "issue"
    extra_context = {"title": "Project2"}
    permission_required = "issue.change_issue"

    def form_valid(self, form):
        form.instance.status = Issue.IssueStatusChoices.CLOSED
        form.instance.date_resolved = timezone.datetime.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("issue-detail", kwargs={"pk": self.get_object().pk})

    def handle_no_permission(self):
        return redirect_no_permission(self)
