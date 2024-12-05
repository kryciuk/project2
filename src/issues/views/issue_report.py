from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import FormView

from communities.models import Building
from core.access_controls_utils import redirect_no_permission
from issues.forms import IssueForm
from issues.models import Issue


class IssueReportView(FormView):
    form_class = IssueForm
    template_name = "issues/issue_report.html"
    extra_context = {"title": "Project2"}
    success_url = reverse_lazy("dashboard-resident")
    permission_required = "issue.add_issue"

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        building = self.kwargs.get("id_building")
        form.instance.building = Building.objects.get(id=building)
        form.instance.status = Issue.IssueStatusChoices.OPEN
        form.instance.reported_by = self.request.user
        form.instance.save()

        form.instance.send_email()

        messages.success(self.request, _("The issue has been reported successfully."))

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["building"] = Building.objects.get(id=self.kwargs.get("id_building"))
        return context

    def handle_no_permission(self):
        return redirect_no_permission(self)
