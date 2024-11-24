from django.urls import path

from .views import IssueCommentView, IssueListView, IssueReportView

urlpatterns = [
    path("building/<int:id_building>/report", IssueReportView.as_view(), name="issue-report"),
    path("", IssueListView.as_view(), name="issue-list"),
    path("<int:pk>", IssueCommentView.as_view(), name="issue-detail"),
]
