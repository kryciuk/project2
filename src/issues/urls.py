from django.urls import path

from .views import IssueDetailView, IssueReportView

urlpatterns = [
    path("<int:id_building>/report", IssueReportView.as_view(), name="issue-report"),
    path("<int:pk>", IssueDetailView.as_view(), name="issue-detail"),
]
