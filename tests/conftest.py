import pytest

from .factories.user import UserFactory

@pytest.fixture
def user():
    return UserFactory()
