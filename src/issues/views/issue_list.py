from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# from core.base import is_member
from issues.models import Issue


class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = "issues/issue_list.html"
    context_object_name = "issues"

    def get_queryset(self):
        # user = self.request.user
        # if is_member(user, "Property Manager"):
        #     queryset = Issue.objects.filter(building__manager=user).all()
        return super().get_queryset()
        # self.filterset = JobOfferFilter(self.request.GET, queryset=queryset)
        # return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["form"] = self.filterset.form
        context["title"] = "Project 2 - Issues"
        return context
