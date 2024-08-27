from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from communities.models import Building
from core.base import is_member

# from core.base import is_member


class BuildingListView(LoginRequiredMixin, ListView):
    model = Building
    template_name = "communities/building_list.html"
    context_object_name = "buildings"
    queryset = Building.objects.all()

    def get_queryset(self):
        user = self.request.user
        if is_member(user, "Property Manager"):
            queryset = Building.objects.filter(manager=user.id).all()
            return queryset
        return super().get_queryset()
        # self.filterset = JobOfferFilter(self.request.GET, queryset=queryset)
        # return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["form"] = self.filterset.form
        context["title"] = "Project 2"
        return context
