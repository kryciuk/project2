from django.urls import path

from users.views import InviteSendView, RegisterView, UserLoginView

urlpatterns = [
    path("invite", InviteSendView.as_view(), name="invite-send"),
    path("signup", RegisterView.as_view(), name="registration"),
    path("login", UserLoginView.as_view(), name="login"),
]
