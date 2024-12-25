from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from core import settings
from users.views import CustomAcceptInvite

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("building/", include("communities.urls")),
    path("user/", include("users.urls")),
    path("issue/", include("issues.urls")),
    path("dashboards/", include("dashboards.urls")),
    path("invitations/", include("invitations.urls", namespace="invitations")),
    path("qr_code/", include("qr_code.urls", namespace="qr_code")),
    re_path(
        r"^invitations/accept-invite/(?P<key>\w+)/?$",
        CustomAcceptInvite.as_view(),
        name="accept-invite",
    ),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
