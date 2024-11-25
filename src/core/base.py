from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from core.consts import GROUPS


def is_member(user, group):
    return user.groups.filter(name=group).exists()


def redirect_to_dashboard_based_on_group(group):
    match group:
        case GROUPS.GROUP__PROPERTY_MANAGER:
            return HttpResponseRedirect(reverse("dashboard-property-manager"))
        case GROUPS.GROUP__RESIDENT:
            return HttpResponseRedirect(reverse("dashboard-resident"))
        case GROUPS.GROUP__ADMINISTRATOR:
            return HttpResponseRedirect(reverse("dashboard-administrator"))
        case _:
            return HttpResponseRedirect(reverse("login"))


def redirect_no_permission(self):
    if self.request.user.is_authenticated:
        messages.warning(self.request, "You can't access this page.")
        group = self.request.user.groups.first()
        return redirect_to_dashboard_based_on_group(group.name)
    messages.warning(self.request, "You can't access this page.")
    return redirect_to_dashboard_based_on_group("")
