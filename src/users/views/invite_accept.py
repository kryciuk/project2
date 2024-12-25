from invitations.views import AcceptInvite


class CustomAcceptInvite(AcceptInvite):
    def get(self, request, *args, **kwargs):
        request.session["invite_key"] = kwargs.get("key")
        return super().get(request, *args, **kwargs)
