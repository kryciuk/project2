from random import randint

import factory
from django.contrib.auth.models import Group

from users.models import CustomUser


def random_name(group: str):
    return f"username{randint(1, 100000)}-{group}"


class AdministratorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f'{random_name("administrator")}{n}')
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@test.com")
    plaintext_password = factory.PostGenerationMethodCall("set_password", "password")
    phone_number = factory.Faker("phone_number", locale="pl_pl")

    @factory.post_generation
    def set_administrator_status(self, create, extracted, **kwargs):
        if not create:
            return
        administrator_group = Group.objects.get(name="Administrator")
        administrator_group.user_set.add(self)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        instance.save()


# # python manage.py shell
# # from users.factories import AdministratorFactory
# # x = AdministratorFactory.create_batch(10)
