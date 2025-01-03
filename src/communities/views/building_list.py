from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from communities.models import Building
from core.access_controls_utils import redirect_no_permission


class BuildingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Building
    template_name = "communities/building_list.html"
    context_object_name = "buildings"
    queryset = Building.objects.all()
    extra_context = {"title": "Project 2"}
    permission_required = "communities.view_building"

    def get_queryset(self):
        user = self.request.user
        queryset = Building.objects.filter(manager=user.id).all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["other_buildings"] = Building.objects.exclude(manager=user.id).all()
        return context

    def handle_no_permission(self):
        return redirect_no_permission(self.request)
