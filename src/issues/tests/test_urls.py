from django.test import TestCase
from django.urls import reverse

from communities.factories import BuildingFactory
from issues.factories import IssueFactory
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_resident import ResidentFactory


class TestIssueUrls(TestCase):
    def setUp(self):
        self.administrator = AdministratorFactory.create()
        self.administrator.save()
        self.building = BuildingFactory.create(manager=self.administrator)
        self.building.save()
        self.resident = ResidentFactory.create(building=self.building)
        self.resident.save()

        self.issue = IssueFactory.create(building=self.building, reported_by=self.resident)

        self.urls_administrator_get = {
            "issue-list": reverse("issue-list"),
            "issue-detail": reverse("issue-detail", kwargs={"pk": self.issue.id}),
        }
        self.urls_administrator_post = {
            "issue-close": reverse("issue-close", kwargs={"pk": self.issue.id}),
        }
        self.urls_resident_get = {
            "issue-report": reverse("issue-report", kwargs={"id_building": self.building.id}),
            "issue-detail": reverse("issue-detail", kwargs={"pk": self.issue.id}),
        }
        self.urls_unauthenticated = {
            "issue-list": reverse("issue-list"),
            "issue-detail": reverse("issue-detail", kwargs={"pk": self.issue.id}),
            "issue-report": reverse("issue-report", kwargs={"id_building": self.building.id}),
            "issue-close": reverse("issue-close", kwargs={"pk": self.issue.id}),
        }

    def test_urls_are_callable_by_name_for_administrator(self):
        self.client.force_login(self.administrator)
        for name, url in self.urls_administrator_get.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)
        for name, url in self.urls_administrator_post.items():
            with self.subTest(url_name=name):
                res = self.client.post(url)
                self.assertEqual(res.status_code, 302)

    def test_urls_are_callable_by_name_for_resident(self):
        self.client.force_login(self.resident)
        for name, url in self.urls_resident_get.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)

    def test_urls_are_callable_by_name_for_unauthenticated(self):
        for name, url in self.urls_unauthenticated.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 302)
