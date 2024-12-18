from django.urls import reverse
from django.views.generic import UpdateView

from communities.forms import BuildingForm
from communities.models import Building


class BuildingUpdateView(UpdateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    model = Building

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = "update"
        return context

    def get_success_url(self):
        return reverse("dashboard-administrator")
