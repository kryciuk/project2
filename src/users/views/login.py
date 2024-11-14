from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls.base import reverse
from django.utils.translation import gettext_lazy as _

from core.base import is_member


class UserLoginView(LoginView):
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "title"
        return context

    def form_invalid(self, form):
        messages.warning(self.request, _("Your login details are incorrect."))
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, _("Logged in successfully."))
        return super().form_valid(form)

    def get_success_url(self):
        if is_member(self.request.user, "Administrator"):
            return reverse("dashboard-administrator")
        elif is_member(self.request.user, "Property Manager"):
            return reverse("dashboard-property-manager")
        elif is_member(self.request.user, "Resident"):
            return reverse("dashboard-resident")
