from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView

from users.models import CustomInvitation, CustomUser


class ResidentDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    context_object_name = "resident"
    template_name = "communities/residents/resident_list.html"

    def post(self, request, *args, **kwargs):
        invitation = CustomInvitation.objects.filter(email=CustomUser.objects.get(id=kwargs["pk"]).email)
        invitation.delete()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        id_building = CustomUser.objects.get(id=self.kwargs["pk"]).building.id
        return reverse("resident-list", kwargs={"pk": id_building})
