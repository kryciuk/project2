from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


class ClearSessionOnViewChangeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if "invite_key" in request.session:
            current_view = resolve(request.path).url_name
            allowed_views = ["registration", "accept-invite"]
            if current_view not in allowed_views:
                del request.session["invite_key"]
