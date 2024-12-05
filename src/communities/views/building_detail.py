from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from communities.models import Building
from core.access_controls_utils import redirect_no_permission


class BuildingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "communities/building_detail.html"
    context_object_name = "building"
    model = Building
    extra_context = {"title": "Project 2"}
    permission_required = "building.view_building"

    def get(self, request, *args, **kwargs):
        request.session["id_building"] = kwargs.get("id_building")
        return super().get(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect_no_permission(self)
