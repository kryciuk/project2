from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from communities.models import Building
from core.access_controls_utils import is_member


class BuildingListView(LoginRequiredMixin, ListView):
    model = Building
    template_name = "communities/building_list.html"
    context_object_name = "buildings"
    queryset = Building.objects.all()
    extra_context = {"title": "Project 2"}

    def get_queryset(self):
        user = self.request.user
        if is_member(user, "Property Manager"):
            queryset = Building.objects.filter(manager=user.id).all()
            return queryset
        return super().get_queryset()
