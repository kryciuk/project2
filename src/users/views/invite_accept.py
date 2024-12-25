from invitations.views import AcceptInvite


class CustomAcceptInvite(AcceptInvite):
    def get(self, request, *args, **kwargs):
        request.session["invite_key"] = kwargs.get("key")
        print(f"Invite key set to session: {request.session.get('invite_key')}")
        return super().get(request, *args, **kwargs)
