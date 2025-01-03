from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from core.access_controls_utils import redirect_no_permission
from issues.forms import CommentForm
from issues.models import Comment, Issue
from landing.templatetags.auth_extras import has_group


class CommentAddView(SingleObjectMixin, FormView):
    form_class = CommentForm
    template_name = ""

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        issue = self.kwargs.get("pk")
        form.instance.issue = Issue.objects.get(id=issue)
        form.instance.author = self.request.user

        form.instance.save()

        messages.success(self.request, _("The comment was added successfully."))

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("issue-detail", kwargs={"pk": self.kwargs.get("pk")})


class IssueDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"
    extra_context = {"title": "Project2"}
    permission_required = "issues.view_issue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(issue=self.object).order_by("date")
        context["form"] = CommentForm()
        return context


class IssueCommentView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, View):
    permission_required = "issues.view_issue"

    def get(self, request, *args, **kwargs):
        view = IssueDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentAddView.as_view()
        return view(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect_no_permission(self.request)

    def test_func(self):
        building = Issue.objects.get(pk=self.kwargs.get("pk")).building.id
        if has_group(self.request.user, "Administrator") or has_group(self.request.user, "Property Manager"):
            return True
        return building == self.request.user.building.id
