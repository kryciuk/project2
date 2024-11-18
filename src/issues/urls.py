from django.urls import path

from .views import IssueDetailView, IssueListView, IssueReportView

urlpatterns = [
    path("<int:id_building>/report", IssueReportView.as_view(), name="issue-report"),
    path("", IssueListView.as_view(), name="issue-list"),
    path("<int:pk>", IssueDetailView.as_view(), name="issue-detail"),
]
