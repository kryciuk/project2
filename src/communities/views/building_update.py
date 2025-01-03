from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from communities.forms import BuildingForm
from communities.models import Building
from core.access_controls_utils import redirect_no_permission


class BuildingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    model = Building
    extra_context = {"action": "update", "title": "Project 2"}
    permission_required = "communities.change_building"

    def handle_no_permission(self):
        return redirect_no_permission(self.request)

    def get_success_url(self):
        return reverse("building-update", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, _("Building updated successfully."))
        return super().form_valid(form)
