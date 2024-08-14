from django.contrib import messages
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "title"
        return context

    def form_invalid(self, form):
        messages.warning(self.request, "Your login details are incorrect.")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully.")
        return super().form_valid(form)
