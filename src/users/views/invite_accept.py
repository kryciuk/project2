from invitations.views import AcceptInvite

from core.mixins import NotLoggedInRequiredMixin


class CustomAcceptInvite(NotLoggedInRequiredMixin, AcceptInvite):
    def get(self, request, *args, **kwargs):
        request.session["invite_key"] = kwargs.get("key")
        return super().get(request, *args, **kwargs)
