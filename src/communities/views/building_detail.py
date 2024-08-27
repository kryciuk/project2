from django.views.generic import DetailView

from communities.models import Building


class BuildingDetailView(DetailView):
    template_name = "communities/building_detail.html"
    context_object_name = "building"
    model = Building
