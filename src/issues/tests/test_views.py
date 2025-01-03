from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import activate

from communities.factories import BuildingFactory
from issues.factories import IssueFactory
from issues.models import Comment, Issue
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_resident import ResidentFactory


class TestIssueCloseView(TestCase):
    def setUp(self):
        self.user_with_permission = AdministratorFactory.create()
        self.user_with_permission.user_permissions.add(
            Permission.objects.get(
                codename="change_issue",
                content_type=ContentType.objects.get_for_model(Issue),
            )
        )
        self.user_without_permission = ResidentFactory.create()

        self.issue = IssueFactory.create()

    def test_view_renders_correct_template(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(reverse("issue-close", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "issues/issue_list.html")

    def test_user_without_permission_cannot_access_view(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(reverse("issue-close", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.status_code, 302)

    def test_user_with_permission_can_access_view(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(reverse("issue-close", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.status_code, 200)

    def test_form_valid_updates_status_and_date_resolved(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(
            reverse("issue-close", kwargs={"pk": self.issue.pk}),
            data={"status": Issue.IssueStatusChoices.CLOSED},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        self.issue.refresh_from_db()
        self.assertEqual(self.issue.status, Issue.IssueStatusChoices.CLOSED)
        self.assertIsNotNone(self.issue.date_resolved)
        self.assertAlmostEqual(self.issue.date_resolved, timezone.now(), delta=timezone.timedelta(seconds=1))

    def test_success_url_redirects_to_issue_detail(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(
            reverse("issue-close", kwargs={"pk": self.issue.pk}),
            data={"status": Issue.IssueStatusChoices.CLOSED},
            follow=True,
        )
        self.assertRedirects(response, reverse("issue-detail", kwargs={"pk": self.issue.pk}))

    def test_context_contains_expected_values(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(reverse("issue-close", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.context["title"], "Project2")
        self.assertEqual(response.context["issue"], self.issue)


class IssueCommentView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.issue = IssueFactory.create(building=self.building)

        self.user_resident1 = ResidentFactory.create(building=self.building)
        self.user_resident1.save()

        self.user_resident2 = ResidentFactory.create()
        self.user_resident2.save()

    def test_get_request_calls_issue_detail_view(self):
        self.client.force_login(self.user_administrator)
        response = self.client.get(reverse("issue-detail", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "issues/issue_detail.html")

    def test_post_request_calls_comment_add_view(self):
        self.client.force_login(self.user_administrator)
        data = {"comment": "This is a comment."}
        response = self.client.post(
            reverse("issue-detail", kwargs={"pk": self.issue.pk}),
            data=data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)

    def test_no_permission_redirects_user(self):
        self.client.force_login(self.user_resident2)
        response = self.client.get(reverse("issue-detail", kwargs={"pk": self.issue.pk}))
        self.assertEqual(response.status_code, 302)
