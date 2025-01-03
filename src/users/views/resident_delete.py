from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView

from landing.templatetags.auth_extras import has_group
from users.models import CustomUser


class ResidentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser
    context_object_name = "resident"
    template_name = "users/resident_list.html"
    extra_context = {"title": "Project2"}
    permission_required = "users.delete_customuser"

    def form_valid(self, form):
        if (
            has_group(self.request.user, "Property Manager")
            and not self.object.building.manager.id == self.request.user.id
        ):
            return self.form_invalid(form)
        messages.warning(self.request, _("Resident successfully deleted."))
        return super().form_valid(form)

    def get_success_url(self):
        id_building = CustomUser.objects.get(id=self.kwargs["pk"]).building.id
        return reverse("resident-list", kwargs={"pk": id_building})

    def handle_no_permission(self):
        id_building = CustomUser.objects.get(id=self.kwargs["pk"]).building.id
        messages.warning(self.request, _("You do not have permission to delete this resident."))
        return HttpResponseRedirect(reverse("resident-list", kwargs={"pk": id_building}))
