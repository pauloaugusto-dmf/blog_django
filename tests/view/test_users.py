import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


class TestUserSignupView:
    def test_reverse_resolve(self):
        assert reverse("user:signup") == "/user/signup"
        assert resolve("/user/signup").view_name == "user:signup"


class TestUserProfileView:
    def test_reverse_resolve(self):
        assert reverse("user:profile") == "/user/profile"
        assert resolve("/user/profile").view_name == "user:profile"


class TestUserUpdateView:
    def test_reverse_resolve(self):
        assert reverse("user:update") == "/user/update"
        assert resolve("/user/update").view_name == "user:update"


class TestUserDeleteView:
    def test_reverse_resolve(self):
        assert reverse("user:delete") == "/user/delete"
        assert resolve("/user/delete").view_name == "user:delete"


class TestUserLoginView:
    def test_reverse_resolve(self):
        assert reverse("user:login") == "/user/login"
        assert resolve("/user/login").view_name == "user:login"


class TestUserLogoutView:
    def test_reverse_resolve(self):
        assert reverse("user:logout") == "/user/logout"
        assert resolve("/user/logout").view_name == "user:logout"
