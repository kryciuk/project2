from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from issues.forms import CommentForm
from issues.models import Comment, Issue


class CommentAddView(SingleObjectMixin, FormView):
    form_class = CommentForm
    template_name = "issues/comment_add.html"

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        issue = self.kwargs.get("pk")
        form.instance.issue = Issue.objects.get(id=issue)
        form.instance.author = self.request.user

        form.instance.save()

        messages.success(self.request, _("The comment was added successfully."))

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse("issue-detail", kwargs={"pk": self.kwargs.get("pk")})


class IssueDetailView(DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(issue=self.object)
        context["form"] = CommentForm()
        return context


class IssueCommentView(View):
    def get(self, request, *args, **kwargs):
        view = IssueDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentAddView.as_view()
        return view(request, *args, **kwargs)
