from django.test import TestCase
from django.urls import reverse

from communities.factories import BuildingFactory
from users.factories.factory_administrator import AdministratorFactory
from users.forms import (
    CreateUserForm,
    SendPropertyManagerInvitationForm,
    SendResidentInvitationForm,
)


class TestCreateUserForm(TestCase):
    def setUp(self):
        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.client.force_login(self.user_administrator)
        self.client.post(
            reverse("invite-resident-send"),
            data={"building": self.building.id, "email": "test_resident@test.com"},
            follow=True,
        )

        self.form_data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "email": "test_resident@test.com",
            "password1": "Miksery1!",
            "password2": "Miksery1!",
            "building": self.building.pk,
        }

    def test_if_user_is_registered_if_correct_data(self):
        form = CreateUserForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_if_user_is_not_registered_if_missing_data(self):
        self.form_data.pop("first_name")
        form = CreateUserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_if_user_is_not_registered_if_no_invitation(self):
        self.form_data["email"] = "test_test@test.com"
        form = CreateUserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_if_user_is_not_registered_if_passwords_dont_match(self):
        self.form_data["password2"] = "Miksery2!"
        form = CreateUserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)


class TestSendResidentInvitationForm(TestCase):
    def setUp(self):
        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.form_data = {"email": "test_resident@test.com", "building": self.building.pk}

    def test_if_user_is_registered_if_correct_data(self):
        form = SendResidentInvitationForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_if_user_is_not_registered_if_missing_data(self):
        self.form_data.pop("email")
        form = SendResidentInvitationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)


class TestSendPropertyManagerInvitationForm(TestCase):
    def setUp(self):

        self.form_data = {
            "email": "test_property_manager@test.com",
        }

    def test_if_user_is_registered_if_correct_data(self):
        form = SendPropertyManagerInvitationForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_if_user_is_not_registered_if_missing_data(self):
        self.form_data.pop("email")
        form = SendResidentInvitationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
