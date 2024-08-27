from django.shortcuts import redirect
from django.views.generic import FormView

from users.forms import SendPropertyManagerInvitationForm, SendResidentInvitationForm
from users.models import CustomInvitation


class InviteResidentSendView(FormView):
    template_name = "users/invite_send.html"
    form_class = SendResidentInvitationForm

    def form_valid(self, form):
        email_address = form.instance.email
        invitation = CustomInvitation.objects.filter(email__iexact=email_address).order_by("created").last()
        if invitation is None:
            # Do not use Invitation.objects.create or
            # Invitation.objects.update_or_create, but use Invitation.create
            # instead, because it sets the key to a secure random value
            invitation = CustomInvitation.create(
                email=email_address,
                building=form.instance.building,
                group=CustomInvitation.GroupChoices.GROUP__RESIDENT,
            )
            invitation.send_invitation(request=self.request)
        return redirect("dashboard-property-manager")


class InvitePropertyManagerSendView(FormView):
    template_name = "users/invite_send.html"
    form_class = SendPropertyManagerInvitationForm

    def form_valid(self, form):
        email_address = form.instance.email
        # TODO get_or_create
        invitation = CustomInvitation.objects.filter(email__iexact=email_address).order_by("created").last()
        if invitation is None:
            # Do not use Invitation.objects.create or
            # Invitation.objects.update_or_create, but use Invitation.create
            # instead, because it sets the key to a secure random value
            invitation = CustomInvitation.create(
                email=email_address, group=CustomInvitation.GroupChoices.GROUP__PROPERTY_MANAGER
            )
            invitation.send_invitation(request=self.request)
        return redirect("dashboard-administrator")
