from django.views.generic import DetailView

from issues.models import Issue


class IssueDetailView(DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"
