from django.urls import path

from users.views import (
    InvitePropertyManagerSendView,
    InviteResidentSendView,
    RegisterView,
    ResidentDeleteView,
    ResidentListView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("invite-resident", InviteResidentSendView.as_view(), name="invite-resident-send"),
    path("<int:pk>/residents", ResidentListView.as_view(), name="resident-list"),
    path("resident-delete/<int:pk>", ResidentDeleteView.as_view(), name="resident-delete"),
    path("invite-property-manager", InvitePropertyManagerSendView.as_view(), name="invite-property-manager-send"),
    path("signup", RegisterView.as_view(), name="registration"),
    path("login", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
