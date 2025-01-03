import os

from django.test import TransactionTestCase
from django.urls import reverse
from django.utils.translation import activate

from communities.consts import CHOICES_CITIES
from communities.factories import BuildingFactory
from communities.models import Building
from core import settings
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_property_manager import PropertyManagerFactory
from users.factories.factory_resident import ResidentFactory


class TestBuildingCreateView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user_with_permission = AdministratorFactory.create()
        self.user_without_permission = ResidentFactory.create()

        self.url = reverse("building-create")

    def test_user_with_permission_can_create_building(self):
        self.client.force_login(self.user_with_permission)
        data = {
            "name": "Test Building",
            "description": "A description of the test building.",
            "city": CHOICES_CITIES[10][0],
            "postal_code": "12-345",
            "street": "Test Street",
            "street_number": "10",
            "manager": self.user_with_permission.id,
        }
        response = self.client.post(self.url, data, follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("dashboard-administrator"))
        self.assertEqual(Building.objects.count(), 2)
        self.assertEqual(Building.objects.last().name, "Test Building")
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "Building created successfully.")

    def test_user_without_permission_cannot_create_building(self):
        self.client.force_login(self.user_without_permission)
        data = {
            "name": "Test Building",
            "description": "A description of the test building.",
            "city": CHOICES_CITIES[10][0],
            "postal_code": "12-345",
            "street": "Test Street",
            "street_number": "10",
            "manager": self.user_with_permission.id,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)

    def test_template_and_context(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "communities/building_create.html")
        self.assertEqual(response.context["action"], "create")
        self.assertEqual(response.context["title"], "Project 2")

    def test_no_permission_redirect(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class TestBuildingDetailView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user_with_permission = AdministratorFactory.create()
        self.user_without_permission = ResidentFactory.create()

        self.building = BuildingFactory.create()

        self.url = reverse("building-detail", kwargs={"pk": self.building.id})

    def test_user_with_permission_can_view_building(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "communities/building_detail.html")
        self.assertEqual(response.context["title"], "Project 2")
        self.assertEqual(response.context["building"], self.building)

    def test_user_without_permission_cannot_view_building(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_no_permission_redirect(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_permission_redirect_to_login_for_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse("login"))


class TestBuildingQRDownloadView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user_with_permission = AdministratorFactory.create()
        self.user_without_permission = ResidentFactory.create()

        self.building = BuildingFactory.create()

        self.url = reverse(
            "building-download",
            kwargs={"id_building": self.building.id, "filename": f"building{self.building.id}_qr.png"},
        )

        self.qr_code_path = os.path.join(settings.MEDIA_ROOT, f"building{self.building.id}_qrcode.png")
        self.create_qr_code_file()

    def create_qr_code_file(self):
        with open(self.qr_code_path, "wb") as f:
            f.write(b"Mock QR Code data")

    def test_user_with_permission_can_download_qr_code(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Disposition"], f'attachment; filename="building{self.building.id}_qr.png"')
        self.assertTrue(response.streaming_content)

    def test_user_without_permission_cannot_download_qr_code(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)


class BuildingListViewTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_with_permission = AdministratorFactory.create()
        self.user_with_permission2 = PropertyManagerFactory.create()
        self.user_without_permission = ResidentFactory.create()

        self.building1 = Building.objects.create(name="Building 1", manager=self.user_with_permission)
        self.building2 = Building.objects.create(name="Building 2", manager=self.user_with_permission)
        self.building3 = Building.objects.create(name="Building 3", manager=self.user_with_permission2)

        self.url = reverse("building-list")

    def test_user_with_permission_can_access_building_list(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Building 1")
        self.assertContains(response, "Building 2")
        self.assertTemplateUsed(response, "communities/building_list.html")
        self.assertIn("buildings", response.context)
        self.assertIn("other_buildings", response.context)

    def test_user_without_permission_cannot_access_building_list(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("dashboard-resident"))

    def test_get_queryset_filters_by_manager(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)

        buildings = response.context["buildings"]
        self.assertEqual(len(buildings), 2)

    def test_get_context_data_excludes_user_buildings_from_other_buildings(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)

        other_buildings = response.context["other_buildings"]
        self.assertIn(self.building3, other_buildings)
        self.assertNotIn(self.building1, other_buildings)
        self.assertNotIn(self.building2, other_buildings)


class BuildingUpdateViewTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_with_permission = AdministratorFactory.create()
        self.user_without_permission = ResidentFactory.create()

        self.building = Building.objects.create(name="Building 1", manager=self.user_with_permission)

        self.url = reverse("building-update", kwargs={"pk": self.building.pk})

    def test_user_with_permission_can_access_update_form(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "communities/building_create.html")
        self.assertIn("building", response.context)
        self.assertIn("action", response.context)
        self.assertEqual(response.context["action"], "update")

    def test_user_without_permission_cannot_access_update_form(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_successful_building_update(self):
        self.client.force_login(self.user_with_permission)
        updated_data = {"name": "Updated Building Name", "description": "456 Updated St", "city": CHOICES_CITIES[0][0]}
        response = self.client.post(self.url, updated_data, follow=True)

        print(response.context["form"].errors)

        self.assertEqual(response.status_code, 200)

        self.building.refresh_from_db()
        self.assertEqual(self.building.name, "Updated Building Name")
        self.assertEqual(self.building.description, "456 Updated St")
