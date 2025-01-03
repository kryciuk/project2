from django.test import TestCase

from communities.consts import CHOICES_CITIES
from communities.factories import BuildingFactory
from communities.models import Building
from users.factories.factory_property_manager import PropertyManagerFactory


class TestBuildingFactories(TestCase):
    def test_create_building_via_factory(self):
        building = BuildingFactory.create()
        self.assertEqual(Building.objects.count(), 1)
        self.assertIsInstance(building, Building)
        self.assertIsNotNone(building.name)
        self.assertIsNotNone(building.description)
        self.assertIsNotNone(building.city)
        self.assertIsNotNone(building.postal_code)
        self.assertIsNotNone(building.street)
        self.assertIsNotNone(building.street_number)
        self.assertIsNotNone(building.manager)

    def test_create_building_batch_factory(self):
        buildings = BuildingFactory.create_batch(10)
        self.assertEqual(Building.objects.count(), 10)
        self.assertEqual(len(buildings), 10)
        for building in buildings:
            self.assertIsInstance(building, Building)
            self.assertIsNotNone(building.name)
            self.assertIsNotNone(building.description)
            self.assertIsNotNone(building.city)
            self.assertIsNotNone(building.postal_code)
            self.assertIsNotNone(building.street)
            self.assertIsNotNone(building.street_number)
            self.assertIsNotNone(building.manager)

    def test_random_city_function(self):
        building = BuildingFactory()
        city = building.city
        self.assertIn(city, [choice[0] for choice in CHOICES_CITIES])

    def test_random_postal_code_function(self):
        building = BuildingFactory()
        postal_code = building.postal_code
        self.assertRegex(postal_code, r"^\d{2}-\d{3}$")

    def test_create_building_with_property_manager(self):
        property_manager = PropertyManagerFactory.create()
        building = BuildingFactory.create(manager=property_manager)
        self.assertEqual(building.manager, property_manager)
