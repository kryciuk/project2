from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from users.models import CustomUser


class ResidentListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "communities/residents/resident_list.html"
    context_object_name = "residents"
    extra_context = {"title": "Project 2"}

    def get_queryset(self):
        building = self.kwargs.get("pk")
        queryset = CustomUser.objects.filter(building_id=building).all()
        return queryset
