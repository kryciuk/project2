from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from communities.forms import BuildingForm
from core.access_controls_utils import redirect_no_permission


class BuildingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    extra_context = {"action": "create", "title": "Project 2"}
    success_url = reverse_lazy("dashboard-administrator")
    permission_required = "communities.add_building"

    def form_valid(self, form):
        messages.success(self.request, _("Building created successfully."))
        return super().form_valid(form)

    def handle_no_permission(self):
        # return redirect_no_permission(request=self.request)
        return redirect_no_permission(self)
