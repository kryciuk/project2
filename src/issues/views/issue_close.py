from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView

from issues.forms import IssueCloseForm
from issues.models import Issue


class IssueCloseView(UpdateView):
    model = Issue
    form_class = IssueCloseForm
    template_name = "issues/issue_list.html"
    context_object_name = "issue"

    def form_valid(self, form):
        form.instance.status = Issue.IssueStatusChoices.CLOSED
        form.instance.date_resolved = timezone.datetime.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("issue-detail", kwargs={"pk": self.get_object().pk})
