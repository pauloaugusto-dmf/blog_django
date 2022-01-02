import factory
from factory.declarations import SubFactory

from publication.models import Post, Topic
from .users import UserFactory



class TopicFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Topic


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence', nb_words=4)
    image = factory.Faker('file_name', category='image')
    alt = factory.Faker('sentence', nb_words=2)
    article = factory.Faker('text')
    topic = SubFactory(TopicFactory)
    author = SubFactory(UserFactory)

    class Meta:
        model = Post
    