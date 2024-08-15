from django.urls import path

from .views import BuildingCreateView, BuildingListView, BuildingUpdateView

urlpatterns = [
    path("new", BuildingCreateView.as_view(), name="building-create"),
    path("list", BuildingListView.as_view(), name="building-list"),
    path("<int:pk>/update", BuildingUpdateView.as_view(), name="building-update"),
]
