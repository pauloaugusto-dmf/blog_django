import factory
import factory.fuzzy

from publication.models import Topic


class TopicFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Topic