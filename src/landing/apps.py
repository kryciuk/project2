from django.apps import AppConfig
from django.db.models.signals import post_migrate


class LandingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "landing"

    def ready(self):
        # from users.signals import create_profile  # noqa: F401

        post_migrate.connect(self.populate_models, sender=self)

    def populate_models(self, sender, **kwargs):
        from django.contrib.auth.models import Group

        # administrator

        administrator, _ = Group.objects.get_or_create(name="Administrator")

        # property_manager

        property_manager, _ = Group.objects.get_or_create(name="Property Manager")

        # resident

        resident, _ = Group.objects.get_or_create(name="Resident")
