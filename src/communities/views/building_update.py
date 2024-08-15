from django.views.generic import UpdateView

from communities.forms import BuildingForm
from communities.models import Building


class BuildingUpdateView(UpdateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    model = Building
