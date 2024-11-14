from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from users.forms import CreateUserForm
from users.models import CustomInvitation


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = CreateUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project2 - Registration"
        invite_key = self.request.session.get("invite_key")
        invitation = CustomInvitation.objects.get(key=invite_key)
        context["building"] = invitation.building
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        if not form.is_valid():
            return self.form_invalid(form)
        else:
            invite_key = self.request.session.get("invite_key")
            invitation = CustomInvitation.objects.get(key=invite_key)
            form.instance.building = invitation.building
            self.request.user = form.save()
        group = Group.objects.get(name=invitation.group)
        group.user_set.add(self.request.user)
        messages.success(self.request, _(f"Account created successfully for {self.request.user.username}."))
        return redirect("index")
