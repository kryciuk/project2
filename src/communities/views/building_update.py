from django.urls import reverse_lazy
from django.views.generic import UpdateView

from communities.forms import BuildingForm
from communities.models import Building


class BuildingUpdateView(UpdateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    model = Building
    extra_context = {"action": "update", "title": "Project 2"}
    success_url = reverse_lazy("dashboard-administrator")
