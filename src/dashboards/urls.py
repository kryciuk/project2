from django.urls import path

from .views.dashboard_administrator import AdministratorDashboardView
from .views.dashboard_property_manager import ManagerDashboardView
from .views.dashboard_resident import ResidentDashboardView

urlpatterns = [
    path("property-manager", ManagerDashboardView.as_view(), name="dashboard-property-manager"),
    path("administator", AdministratorDashboardView.as_view(), name="dashboard-administrator"),
    path("resident", ResidentDashboardView.as_view(), name="dashboard-resident"),
]
