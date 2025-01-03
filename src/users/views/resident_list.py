from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from users.models import CustomUser


class ResidentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/resident_list.html"
    context_object_name = "residents"
    extra_context = {"title": "Project 2"}
    permission_required = "communities.view_building"

    def get_queryset(self):
        building = self.kwargs.get("pk")
        queryset = CustomUser.objects.filter(building_id=building).all()
        return queryset
