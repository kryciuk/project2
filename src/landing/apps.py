from django.apps import AppConfig
from django.db.models.signals import post_migrate

from core.utils import _get_perms_for_models


class LandingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "landing"

    def ready(self):
        post_migrate.connect(self.populate_models, sender=self)

    def populate_models(self, sender, **kwargs):
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        from communities.models import Building
        from issues.models import Comment, Issue

        # all model permissions

        models_to_fetch_administrator = [Building, Issue, Comment]
        models_to_fetch_property_manager = [Issue]

        # single permissions

        content_type_profile = ContentType.objects.get_for_model(Building)

        permission_update_building = Permission.objects.get(
            codename="change_building", content_type=content_type_profile
        )
        permission_view_building = Permission.objects.get(codename="view_building", content_type=content_type_profile)
        permission_add_issue = Permission.objects.get(codename="add_issue", content_type=content_type_profile)
        permission_view_issue = Permission.objects.get(codename="view_issue", content_type=content_type_profile)
        permission_add_comment = Permission.objects.get(codename="add_comment", content_type=content_type_profile)

        # administrator

        administrator, _ = Group.objects.get_or_create(name="Administrator")
        administrator.permissions.set(_get_perms_for_models(models_to_fetch_administrator))

        # property_manager

        property_manager, _ = Group.objects.get_or_create(name="Property Manager")
        administrator.permissions.set(_get_perms_for_models(models_to_fetch_property_manager))
        property_manager.permissions.add(
            [permission_update_building, permission_view_building, permission_add_comment]
        )

        # resident

        resident, _ = Group.objects.get_or_create(name="Resident")
        property_manager.permissions.add([permission_add_issue, permission_view_issue, permission_add_comment])
