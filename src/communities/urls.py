from django.urls import path

from .views import (
    BuildingCreateView,
    BuildingDetailView,
    BuildingListView,
    BuildingUpdateView,
)
from .views.residents import ResidentListView

urlpatterns = [
    path("new", BuildingCreateView.as_view(), name="building-create"),
    path("list", BuildingListView.as_view(), name="building-list"),
    path("<int:pk>", BuildingDetailView.as_view(), name="building-detail"),
    path("<int:pk>/update", BuildingUpdateView.as_view(), name="building-update"),
    path("<int:pk>/residents", ResidentListView.as_view(), name="resident-list"),
]
