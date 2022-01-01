import pytest

from .factories.users import UserFactory
from .factories.publication import TopicFactory

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def topic():
    return TopicFactory()
