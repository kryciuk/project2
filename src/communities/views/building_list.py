from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from communities.models import Building
from core.access_controls_utils import is_member, redirect_no_permission


class BuildingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Building
    template_name = "communities/building_list.html"
    context_object_name = "buildings"
    queryset = Building.objects.all()
    extra_context = {"title": "Project 2"}
    permission_required = "communities.view_building"

    def get_queryset(self):
        user = self.request.user
        if is_member(user, "Property Manager"):
            queryset = Building.objects.filter(manager=user.id).all()
            return queryset
        return super().get_queryset()

    def handle_no_permission(self):
        return redirect_no_permission(self)
