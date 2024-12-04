import factory
from factory.fuzzy import FuzzyChoice

from issues.models import Comment, Issue
from users.factories_resident import ResidentFactory
from users.models import CustomUser


class IssueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Issue

    title = factory.Faker("word")
    description = factory.Faker("paragraph", locale="pl_pl")
    reported_by = factory.SubFactory(ResidentFactory)
    building = factory.SelfAttribute("reported_by.building")
    place = FuzzyChoice(choices=Issue.IssuePlaceChoices.choices, getter=lambda x: x[0])
    severity = FuzzyChoice(choices=Issue.IssueSeverityChoices.choices, getter=lambda x: x[0])
    status = FuzzyChoice(choices=Issue.IssueStatusChoices.choices, getter=lambda x: x[0])


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    comment = factory.Faker("paragraph", locale="pl_pl")
    issue = factory.SubFactory(IssueFactory)
    author = factory.SelfAttribute("issue.building.residents")

    @factory.lazy_attribute
    def author(self):
        building = self.issue.building
        return CustomUser.objects.filter(building=building).order_by("?").first()


# python manage.py shell
# from issues.factories import IssueFactory, CommentFactory
# x = IssueFactory.create_batch(10)
