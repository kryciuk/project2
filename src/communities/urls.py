from django.urls import path

from .views import BuildingCreateView

urlpatterns = [
    path("new", BuildingCreateView.as_view(), name="building-create"),
]