from django.test import TransactionTestCase
from django.urls import reverse
from django.utils.translation import activate

from communities.factories import BuildingFactory
from landing.templatetags.auth_extras import has_group
from users.factories.factory_administrator import AdministratorFactory
from users.factories.factory_property_manager import PropertyManagerFactory
from users.factories.factory_resident import ResidentFactory
from users.models import CustomInvitation, CustomUser


class TestInviteResidentSendView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

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
        response = self.client.post(
            reverse("invite-resident-send"), data={"building": building.id, "email": "test@test.com"}, follow=True
        )
        self.assertEqual(CustomInvitation.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("dashboard-property-manager"))

    def test_administrator_can_send_invitation_and_is_redirected(self):
        building = BuildingFactory.create(manager=self.user_administrator)
        self.client.force_login(self.user_administrator)
        response = self.client.post(
            reverse("invite-resident-send"), data={"building": building.id, "email": "test@test.com"}, follow=True
        )
        self.assertEqual(CustomInvitation.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("dashboard-administrator"))


class TestInviteAcceptView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.user_property_manager = PropertyManagerFactory.create()
        self.user_property_manager.save()

        self.user_resident = ResidentFactory.create()
        self.user_resident.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.client.force_login(self.user_administrator)
        self.client.post(
            reverse("invite-resident-send"), data={"building": self.building.id, "email": "test@test.com"}, follow=True
        )
        self.client.logout()

    def test_user_is_redirected_and_key_is_stored(self):
        invitation = CustomInvitation.objects.get(email="test@test.com")
        response = self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        request = response.wsgi_request
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.session["invite_key"], invitation.key)
        self.assertRedirects(response, reverse("registration"))

    def test_logged_user_cant_access_view(self):
        self.client.force_login(self.user_administrator)
        invitation = CustomInvitation.objects.get(email="test@test.com")
        response = self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        self.assertRedirects(response, reverse("dashboard-administrator"))


class TestLoginView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.user_property_manager = PropertyManagerFactory.create()
        self.user_property_manager.save()

    def test_login_denied_wrong_password(self):
        login_wrong_password = self.client.login(username=self.user_administrator.username, password="wrong_password")
        self.assertFalse(login_wrong_password)

    def test_login_success_right_password(self):
        login_right_password = self.client.login(username=self.user_administrator.username, password="password")
        self.assertTrue(login_right_password)

    def test_login_redirects_to_dashboard_after_successful_login(self):
        response_administrator = self.client.post(
            reverse("login"), {"username": self.user_administrator.username, "password": "password"}
        )
        self.assertEqual(response_administrator.status_code, 302)
        response_property_manager = self.client.post(
            reverse("login"), {"username": self.user_property_manager.username, "password": "password"}
        )
        self.assertEqual(response_property_manager.status_code, 302)

    def test_login_redirects_to_dashboard_when_logged_user(self):
        self.client.force_login(self.user_administrator)
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 302)

    def test_correct_template_is_used(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "users/login.html")

    def test_message_are_shown_after_successful_or_unsuccessful_login(self):
        response_successful_login = self.client.post(
            reverse("login"), {"username": self.user_administrator.username, "password": "password"}, follow=True
        )
        message = list(response_successful_login.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "Logged in successfully.")
        self.client.logout()

        response_unsuccessful_login = self.client.post(
            reverse("login"), {"username": self.user_administrator.username, "password": "wrong_password"}, follow=True
        )
        message = list(response_unsuccessful_login.context.get("messages"))[0]
        self.assertEqual(message.tags, "warning")
        self.assertEqual(message.message, "Your login details are incorrect.")
        self.client.logout()


class TestLogoutView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

    def test_if_logges_out_user(self):
        self.client.force_login(self.user_administrator)
        response = self.client.post(reverse("logout"))
        request = response.wsgi_request
        self.assertEqual(request.user.is_authenticated, False)


class TestRegistrationView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

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
        self.client.post(
            reverse("invite-property-manager-send"), data={"email": "test_property_manager@test.com"}, follow=True
        )
        self.client.logout()

        self.data = {
            "username": "testuser",
            "first_name": "John",
            "last_name": "Smith",
            "email": "test_resident@test.com",
            "password1": "Miksery1!",
            "password2": "Miksery1!",
        }

    def test_if_registers_resident_correctly(self):
        invitation = CustomInvitation.objects.get(email="test_resident@test.com")
        self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        self.client.post(reverse("registration"), data=self.data)
        created_user = CustomUser.objects.get(username="testuser")
        self.assertTrue(created_user)
        self.assertTrue(has_group(created_user, "Resident"))

    def test_if_registers_employee_correctly(self):
        self.data["email"] = "test_property_manager@test.com"
        invitation = CustomInvitation.objects.get(email="test_property_manager@test.com")
        self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        self.client.post(reverse("registration"), data=self.data)
        created_user = CustomUser.objects.get(username="testuser")
        self.assertTrue(created_user)
        self.assertTrue(has_group(created_user, "Property Manager"))

    def test_if_registration_fails_if_incorrect_data(self):
        self.data["email"] = ""
        invitation = CustomInvitation.objects.get(email="test_resident@test.com")
        self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        self.client.post(reverse("registration"), data=self.data)
        created_user = CustomUser.objects.filter(username="testuser").first()
        self.assertFalse(created_user)

    def test_message_is_shown_after_successful_registration(self):
        invitation = CustomInvitation.objects.get(email="test_resident@test.com")
        self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        response = self.client.post(reverse("registration"), data=self.data, follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, f"Account created successfully for {self.data.get('username')}.")

    def test_correct_template_is_used(self):
        invitation = CustomInvitation.objects.get(email="test_resident@test.com")
        self.client.get(reverse("accept-invite", kwargs={"key": invitation.key}), follow=True)
        response = self.client.get(reverse("registration"))
        self.assertTemplateUsed(response, "users/registration.html")


class TestResidentDeleteView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.user_property_manager = PropertyManagerFactory.create()
        self.user_property_manager.save()

        self.building_administrator = BuildingFactory.create(manager=self.user_administrator)
        self.building_administrator.save()

        self.building_property_manager = BuildingFactory.create(manager=self.user_property_manager)
        self.building_property_manager.save()

        self.user_resident1 = ResidentFactory.create(building=self.building_administrator)
        self.user_resident1.save()

        self.user_resident2 = ResidentFactory.create(building=self.building_property_manager)
        self.user_resident2.save()

    def test_if_administrator_deletes_residents_correctly(self):
        self.client.force_login(self.user_administrator)
        self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident1.id}), follow=True)
        self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident2.id}), follow=True)
        self.assertFalse(CustomUser.objects.filter(pk=self.user_resident1.id).exists())
        self.assertFalse(CustomUser.objects.filter(pk=self.user_resident2.id).exists())

    def test_if_property_manager_can_delete_only_own_residents(self):
        self.client.force_login(self.user_property_manager)
        self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident1.id}), follow=True)
        self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident2.id}), follow=True)
        self.assertTrue(CustomUser.objects.filter(pk=self.user_resident1.id).exists())
        self.assertFalse(CustomUser.objects.filter(pk=self.user_resident2.id).exists())

    def test_message_is_shown_after_successful_deletion(self):
        self.client.force_login(self.user_administrator)
        response = self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident1.id}), follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "warning")
        self.assertEqual(message.message, "Resident successfully deleted.")

    def test_if_user_is_redirected_after_successful_deletion(self):
        self.client.force_login(self.user_administrator)
        building_id = self.user_resident1.building.id
        response = self.client.post(reverse("resident-delete", kwargs={"pk": self.user_resident1.id}), follow=True)
        self.assertRedirects(response, reverse("resident-list", kwargs={"pk": building_id}))


class TestResidentListView(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        activate("en")

        self.user_administrator = AdministratorFactory.create()
        self.user_administrator.save()

        self.building = BuildingFactory.create(manager=self.user_administrator)
        self.building.save()

        self.user_residents = ResidentFactory.create_batch(5, building=self.building)
        for user in self.user_residents:
            user.save()

    def test_if_users_are_shown_on_the_list(self):
        self.client.force_login(self.user_administrator)
        response = self.client.get(reverse("resident-list", kwargs={"pk": self.building.id}))
        self.assertCountEqual(response.context["object_list"], self.user_residents)

    def test_correct_template_is_used(self):
        self.client.force_login(self.user_administrator)
        response = self.client.get(reverse("resident-list", kwargs={"pk": self.building.id}))
        self.assertTemplateUsed(response, "users/resident_list.html")
