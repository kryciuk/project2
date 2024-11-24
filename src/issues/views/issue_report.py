from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import FormView

from communities.models import Building
from issues.forms import IssueForm
from issues.models import Issue


class IssueReportView(FormView):
    form_class = IssueForm
    template_name = "issues/issue_report.html"

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

    def get_success_url(self):
        return reverse("dashboard-resident")
