from django.core.mail import send_mail
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import FormView

from communities.models import Building
from issues.forms import IssueForm
from issues.models import Issue
from users.models import CustomUser


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

        # sending email to property manager
        subject = _(f"New issue in building {form.instance.building}. Level: {form.instance.severity}")
        message = _(f"New issue in building {form.instance.building}. Description: {form.instance.description}")
        from_email = "default"
        if form.instance.building.manager is None:
            recipient_list = [user.email for user in CustomUser.objects.filter(groups__name="Administrator")]
        else:
            recipient_list = [form.instance.building.manager.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("dashboard-property-manager")
