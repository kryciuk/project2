from django.contrib.auth.models import Group
from django.test import Client, TestCase
from django.urls import reverse

from users.models import CustomUser


class TestCommunitiesViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client(HTTP_HOST="localhost:8000")

        user = CustomUser.objects.create(username="test_user1", email="test_user1@test.com")
        user.set_password("password")
        user.save()

        cls.user = user
        administrator, _ = Group.objects.get_or_create(name="Administrator")
        administrator.user_set.add(user)

    def test_template_name_correct(self):
        self.client.login(username=self.user.username, password="password")
        response = self.client.get(reverse("dashboard-administrator"), {"user_id": self.user.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboards/dashboard_administrator.html")
