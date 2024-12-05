from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
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
    success_url = reverse_lazy("dashboard-administrator")
    permission_required = "building.change_building"

    def handle_no_permission(self):
        return redirect_no_permission(self)
