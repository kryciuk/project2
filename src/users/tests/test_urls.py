from django.test import TestCase
from django.urls import reverse

from communities.factories import BuildingFactory
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_resident import ResidentFactory


class TestUrls(TestCase):
    def setUp(self):
        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()
        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()
        self.user_resident = ResidentFactory.create(building=self.building)
        self.user_resident.save()

        self.urls_administrator_get = {
            "invite-resident-send": reverse("invite-resident-send"),
            "resident-list": reverse("resident-list", kwargs={"pk": self.building.id}),
            "invite-property-manager-send": reverse("invite-property-manager-send"),
        }

        self.urls_administrator_post = {
            "resident-delete": reverse("resident-delete", kwargs={"pk": self.user_resident.id}),
            "logout": reverse("logout"),
        }

        self.urls_unauthenticated = {
            "login": reverse("login"),
        }

    def test_urls_are_callable_by_name_for_administrator(self):
        self.client.force_login(self.user_administrator)
        for name, url in self.urls_administrator_get.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)
        for name, url in self.urls_administrator_post.items():
            with self.subTest(url_name=name):
                res = self.client.post(url)
                self.assertEqual(res.status_code, 302)

    def test_urls_are_callable_by_name_for_unauthenticated(self):
        for name, url in self.urls_unauthenticated.items():
            with self.subTest(url_name=name):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)
