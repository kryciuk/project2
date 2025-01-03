from random import randint

import factory
from django.contrib.auth.models import Group

from communities.factories import BuildingFactory
from users.models import CustomUser


def random_name(group: str):
    return f"username{randint(1, 100000)}-{group}"


class ResidentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f'{random_name("resident")}{n}')
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@test.com")
    plaintext_password = factory.PostGenerationMethodCall("set_password", "password")
    phone_number = factory.Faker("phone_number", locale="pl_pl")
    building = factory.SubFactory(BuildingFactory)

    @factory.post_generation
    def set_resident_status(self, create, extracted, **kwargs):
        if not create:
            return
        resident_group = Group.objects.get(name="Resident")
        resident_group.user_set.add(self)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        instance.save()


# # python manage.py shell
# # from users.factories import AdministratorFactory
# # x = AdministratorFactory.create_batch(10)
