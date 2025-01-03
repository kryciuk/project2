from django.test import TestCase
from django.urls import reverse

from communities.factories import BuildingFactory
from users.factories.factory_administrator import AdministratorFactory


class TestBuildingUrls(TestCase):
    def setUp(self):
        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.urls_administrator_get = {
            "building-create": reverse("building-create"),
            "building-list": reverse("building-list"),
            "building-detail": reverse("building-detail", kwargs={"pk": self.building.id}),
            "building-update": reverse("building-update", kwargs={"pk": self.building.id}),
            "building-download": reverse(
                "building-download", kwargs={"id_building": self.building.id, "filename": "qr_code.png"}
            ),
        }

    def test_urls_are_callable_by_name_for_administrator(self):
        self.client.force_login(self.user_administrator)

        for name, url in self.urls_administrator_get.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)

    def test_urls_are_callable_by_name_for_unauthenticated(self):
        unauthenticated_urls = {
            "building-list": reverse("building-list"),
            "building-detail": reverse("building-detail", kwargs={"pk": self.building.id}),
        }

        for name, url in unauthenticated_urls.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 302)
                self.assertRedirects(res, reverse("login"))

    def test_urls_are_callable_for_invalid_building(self):
        invalid_urls = {
            "building-detail": reverse("building-detail", kwargs={"pk": 99999}),
            "building-update": reverse("building-update", kwargs={"pk": 99999}),
            "building-download": reverse(
                "building-download", kwargs={"id_building": 99999, "filename": "invalid.png"}
            ),
        }

        for name, url in invalid_urls.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 302)
