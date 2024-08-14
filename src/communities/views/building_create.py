from django.views.generic import CreateView

from communities.models import Building
from communities.forms import BuildingForm


class BuildingCreateView(CreateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
