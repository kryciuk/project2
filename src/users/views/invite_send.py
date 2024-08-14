from django.shortcuts import redirect
from django.views.generic import FormView

from users.forms import SendInvitationForm
from users.models import CustomInvitation


class InviteSendView(FormView):
    template_name = "users/base.html"
    form_class = SendInvitationForm

    def form_valid(self, form):
        email_address = form.instance.email
        invitation = CustomInvitation.objects.filter(email__iexact=email_address).order_by("created").last()
        if invitation is None:
            # Do not use Invitation.objects.create or
            # Invitation.objects.update_or_create, but use Invitation.create
            # instead, because it sets the key to a secure random value
            invitation = CustomInvitation.create(email=email_address, building=form.instance.building)
            invitation.send_invitation(request=self.request)
        return redirect("index")
