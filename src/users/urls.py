from django.urls import path

from users.views import (
    InvitePropertyManagerSendView,
    InviteResidentSendView,
    RegisterView,
    UserLoginView,
)

urlpatterns = [
    path("invite-resident", InviteResidentSendView.as_view(), name="invite-resident-send"),
    path("invite-property-manager", InvitePropertyManagerSendView.as_view(), name="invite-property-manager-send"),
    path("signup", RegisterView.as_view(), name="registration"),
    path("login", UserLoginView.as_view(), name="login"),
]
