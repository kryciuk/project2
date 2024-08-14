"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from core import settings
from users.views import CustomAcceptInvite

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("building/", include("communities.urls")),
    path("user/", include("users.urls")),
    re_path(
        r"^invitations/accept-invite/(?P<key>\w+)/?$",
        CustomAcceptInvite.as_view(),
        name="accept-invite",
    ),
    # path('dashboards/', include("dashboards.urls")),
    path("invitations/", include("invitations.urls", namespace="invitations")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
