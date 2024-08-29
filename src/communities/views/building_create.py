from django.urls import reverse
from django.views.generic import CreateView

from communities.forms import BuildingForm


class BuildingCreateView(CreateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm

    def get_success_url(self):
        return reverse("dashboard-administrator")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = "create"
        return context
