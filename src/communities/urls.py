from django.urls import path

from .views import (
    BuildingCreateView,
    BuildingDetailView,
    BuildingListView,
    BuildingQRDownloadView,
    BuildingUpdateView,
)

urlpatterns = [
    path("new", BuildingCreateView.as_view(), name="building-create"),
    path("list", BuildingListView.as_view(), name="building-list"),
    path("<int:pk>", BuildingDetailView.as_view(), name="building-detail"),
    path("<int:pk>/update", BuildingUpdateView.as_view(), name="building-update"),
    path("<int:id_building>/download/<str:filename>/", BuildingQRDownloadView.as_view(), name="building-download"),
]
