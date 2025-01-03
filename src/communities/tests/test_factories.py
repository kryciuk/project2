from django.test import TestCase

from issues.factories import CommentFactory, IssueFactory
from issues.models import Comment, Issue
from users.models import CustomUser


class TestIssueAndCommentFactories(TestCase):
    def test_create_issue_via_factory(self):
        issue = IssueFactory.create()
        self.assertEqual(Issue.objects.count(), 1)
        self.assertEqual(issue.reported_by.groups.first().name, "Resident")

    def test_create_issue_batch_factory(self):
        IssueFactory.create_batch(5)
        self.assertEqual(Issue.objects.count(), 5)

    def test_issue_factory_attributes(self):
        issue = IssueFactory.create()
        self.assertIsNotNone(issue.title)
        self.assertIsNotNone(issue.description)
        self.assertIn(issue.place, dict(Issue.IssuePlaceChoices.choices).keys())
        self.assertIn(issue.severity, dict(Issue.IssueSeverityChoices.choices).keys())
        self.assertIn(issue.status, dict(Issue.IssueStatusChoices.choices).keys())

    def test_create_comment_via_factory(self):
        comment = CommentFactory.create()
        self.assertEqual(Comment.objects.count(), 1)
        self.assertIsNotNone(comment.comment)
        self.assertIsNotNone(comment.issue)
        self.assertIn(comment.author, CustomUser.objects.filter(building=comment.issue.building))

    def test_create_comment_batch_factory(self):
        CommentFactory.create_batch(5)
        self.assertEqual(Comment.objects.count(), 5)

    def test_comment_factory_relationship(self):
        issue = IssueFactory.create()
        comment = CommentFactory.create(issue=issue)
        self.assertEqual(comment.issue, issue)
        self.assertIn(comment.author, CustomUser.objects.filter(building=issue.building))

    def test_issue_and_comment_integration(self):
        issue = IssueFactory.create()
        CommentFactory.create_batch(3, issue=issue)
        self.assertEqual(issue.comment_set.count(), 3)
