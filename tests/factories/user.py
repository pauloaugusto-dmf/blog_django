import factory
import factory.fuzzy

from users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText()
    email = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()

    class Meta:
        model = User