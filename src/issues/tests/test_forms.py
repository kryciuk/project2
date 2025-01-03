from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

from issues.forms import CommentForm, IssueCloseForm, IssueForm
from issues.models import Issue


class TestIssueForm(TestCase):
    def setUp(self):
        self.valid_data = {
            "title": "Broken Pipe",
            "description": "There is a broken pipe in the garage.",
            "place": Issue.IssuePlaceChoices.GARAGE,
            "severity": Issue.IssueSeverityChoices.HIGH,
            "photo": SimpleUploadedFile(
                name="test_image.jpg",
                content=b"file_content",
                content_type="image/jpeg",
            ),
        }

    def test_form_is_valid_with_correct_data(self):
        form = IssueForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_missing_required_field(self):
        self.valid_data.pop("title")
        form = IssueForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)


class TestIssueCloseForm(TestCase):
    def setUp(self):
        self.valid_data = {"status": Issue.IssueStatusChoices.CLOSED, "date_resolved": timezone.now()}

    def test_form_is_valid_with_correct_data(self):
        form = IssueCloseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_invalid_date_format(self):
        self.valid_data["date_resolved"] = "invalid_date"
        form = IssueCloseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("date_resolved", form.errors)


class TestCommentForm(TestCase):
    def setUp(self):
        self.valid_data = {"comment": "This is a test comment."}

    def test_form_is_valid_with_correct_data(self):
        form = CommentForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_empty_comment(self):
        self.valid_data["comment"] = ""
        form = CommentForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("comment", form.errors)
