from django.test import TestCase

from communities.consts import CHOICES_CITIES
from communities.factories import BuildingFactory
from communities.forms import BuildingForm
from users.factories.factory_administrator import AdministratorFactory


class TestBuildingForm(TestCase):
    def setUp(self):
        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.form_data = {
            "name": "Test Building",
            "description": "A description of the test building.",
            "city": CHOICES_CITIES[10][0],
            "postal_code": "12-345",
            "street": "Test Street",
            "street_number": "10",
            "manager": self.user_administrator.pk,
        }

    def test_if_building_form_is_valid_with_correct_data(self):
        form = BuildingForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_if_building_form_is_invalid_with_missing_data(self):
        self.form_data.pop("name")
        form = BuildingForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_if_building_form_is_invalid_with_invalid_postal_code(self):
        self.form_data["postal_code"] = "1234"
        form = BuildingForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_if_building_form_creates_building_instance(self):
        form = BuildingForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        building_instance = form.save()
        self.assertEqual(building_instance.name, self.form_data["name"])
        self.assertEqual(building_instance.manager, self.user_administrator)
        self.assertEqual(building_instance.city, self.form_data["city"])

    def test_if_building_form_has_correct_labels(self):
        form = BuildingForm(data=self.form_data)
        self.assertEqual(form.fields["name"].label, "Name")
        self.assertEqual(form.fields["description"].label, "Description")
        self.assertEqual(form.fields["city"].label, "City")
        self.assertEqual(form.fields["postal_code"].label, "Postal code")
        self.assertEqual(form.fields["street"].label, "Street")
        self.assertEqual(form.fields["street_number"].label, "Building number")
        self.assertEqual(form.fields["manager"].label, "Property Manager")
