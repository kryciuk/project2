from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class UserLogoutView(LogoutView):
    extra_context = {"title": "Project2"}

    def get_success_url(self):
        return reverse("login")

    def post(self, request, *args, **kwargs):
        messages.success(self.request, _("Logged out successfully."))
        return super().post(request, *args, **kwargs)
