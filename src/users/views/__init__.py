from .invite_accept import CustomAcceptInvite
from .invite_send import InvitePropertyManagerSendView, InviteResidentSendView
from .login import UserLoginView
from .logout import UserLogoutView
from .registration import RegisterView
from .resident_delete import ResidentDeleteView
from .resident_list import ResidentListView

__all__ = [
    "InviteResidentSendView",
    "ResidentListView",
    "ResidentDeleteView",
    "InvitePropertyManagerSendView",
    "RegisterView",
    "UserLoginView",
    "CustomAcceptInvite",
    "UserLogoutView",
]
