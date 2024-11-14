from django.contrib.auth.views import LogoutView
from django.shortcuts import reverse


class UserLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Logout"
        return context

    def get_success_url(self):
        return reverse("login")
