from django.test import TestCase

from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_property_manager import PropertyManagerFactory
from users.factories.factory_resident import ResidentFactory
from users.models import CustomUser


class TestUserFactories(TestCase):
    def test_create_administrator_via_factory(self):
        AdministratorFactory.create()
        self.assertEqual(CustomUser.objects.filter(groups__name="Administrator").count(), 1)

    def test_create_administrator_batch_factory(self):
        AdministratorFactory.create_batch(5)
        self.assertEqual(CustomUser.objects.filter(groups__name="Administrator").count(), 5)

    def test_create_property_manager_via_factory(self):
        PropertyManagerFactory.create()
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.filter(groups__name="Property Manager").count(), 1)

    def test_create_property_manager_batch_factory(self):
        PropertyManagerFactory.create_batch(5)
        self.assertEqual(CustomUser.objects.filter(groups__name="Property Manager").count(), 5)

    def test_create_resident_via_factory(self):
        ResidentFactory.create()
        self.assertEqual(CustomUser.objects.filter(groups__name="Resident").count(), 1)

    def test_create_resident_batch_factory(self):
        ResidentFactory.create_batch(5)
        self.assertEqual(CustomUser.objects.filter(groups__name="Resident").count(), 5)
