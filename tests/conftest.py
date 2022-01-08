import pytest

from .factories.users import UserFactory
from .factories.publication import TopicFactory, PostFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def topic():
    return TopicFactory()


@pytest.fixture
def post():
    return PostFactory()
