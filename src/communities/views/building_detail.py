from django.views.generic import DetailView

from communities.models import Building

class BuildingDetailView(DetailView):
    template_name = "communities/building_detail.html"
    context_object_name = "building"
    model = Building
    extra_context = {"title": "Project 2"}

    def get(self, request, *args, **kwargs):
        request.session["id_building"] = kwargs.get("id_building")
        return super().get(request, *args, **kwargs)
