from django.contrib.auth.models import Group
from django.test import Client, TestCase, TransactionTestCase, tag
from django.urls import reverse
from django.utils.translation import activate
import pytest
from requests import session

from communities.factories import BuildingFactory
from landing.templatetags.auth_extras import has_group
from users.factories.factory_resident import ResidentFactory
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_property_manager import PropertyManagerFactory
from users.models import CustomInvitation


class TestInviteResidentSendView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate('en')

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.user_property_manager = PropertyManagerFactory.create()
        self.user_property_manager.save()

        self.user_resident = ResidentFactory.create()
        self.user_resident.save()

    def test_administrator_can_access_view(self):
        self.client.force_login(self.user_administrator)
        response = self.client.get(reverse("invite-resident-send"))
        self.assertEqual(response.status_code, 200)

    def test_property_manager_can_access_view(self):
        self.client.force_login(self.user_property_manager)
        response = self.client.get(reverse("invite-resident-send"))
        self.assertEqual(response.status_code, 200)

    def test_resident_cant_access_view(self):
        self.client.force_login(self.user_resident)
        response = self.client.get(reverse("invite-resident-send"))
        self.assertEqual(response.status_code, 403)

    def test_property_manager_can_send_invitation_and_is_redirected(self):
        building = BuildingFactory.create(manager=self.user_property_manager)
        self.client.force_login(self.user_property_manager)
        response = self.client.post(reverse("invite-resident-send"), data={"building": building.id, "email": "test@test.com"}, follow=True)
        self.assertEqual(CustomInvitation.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("dashboard-property-manager"))

    def test_administrator_can_send_invitation_and_is_redirected(self):
        building = BuildingFactory.create(manager=self.user_administrator)
        self.client.force_login(self.user_administrator)
        response = self.client.post(reverse("invite-resident-send"), data={"building": building.id, "email": "test@test.com"}, follow=True)
        self.assertEqual(CustomInvitation.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("dashboard-administrator"))


class TestInviteAcceptView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate('en')

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.user_property_manager = PropertyManagerFactory.create()
        self.user_property_manager.save()

        self.user_resident = ResidentFactory.create()
        self.user_resident.save()

    @tag("x")
    def test_invitation_key_is_redirected(self):
        building = BuildingFactory.create(manager=self.user_administrator)
        self.client.force_login(self.user_administrator)
        self.client.post(reverse("invite-resident-send"), data={"building": building.id, "email": "test@test.com"}, follow=True)
        invitation = CustomInvitation.objects.get(email="test@test.com")
        self.client.logout()
        print(invitation.key)
        response = self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        print(response.__dict__)
