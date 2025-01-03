from random import randint

import factory

from communities.consts import CHOICES_CITIES
from communities.models import Building
from users.factories.factory_property_manager import PropertyManagerFactory


def random_postal_code():
    return f"{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}"


def random_city():
    return CHOICES_CITIES[randint(0, len(CHOICES_CITIES) - 1)][0]


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    name = factory.Faker("word")
    description = factory.Faker("paragraph", locale="pl_pl")
    city = factory.LazyFunction(random_city)
    postal_code = factory.LazyFunction(random_postal_code)
    street = factory.Faker("street_name")
    street_number = factory.LazyFunction(lambda: randint(1, 100))
    manager = factory.SubFactory(PropertyManagerFactory)


# python manage.py shell
# from communities.factories import BuildingFactory
# x = BuildingFactory.create_batch(10)
