from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from communities.forms import BuildingForm


class BuildingCreateView(CreateView):
    template_name = "communities/building_create.html"
    context_object_name = "building"
    form_class = BuildingForm
    extra_context = {"action": "create", "title": "Project 2"}
    success_url = reverse_lazy("dashboard-administrator")

    def form_valid(self, form):
        messages.success(self.request, _("Building created successfully."))
        return super().form_valid(form)
