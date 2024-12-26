from django.contrib.auth.mixins import AccessMixin

from core.access_controls_utils import redirect_no_permission


class NotLoggedInRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect_no_permission(request)
        return super().dispatch(request, *args, **kwargs)
