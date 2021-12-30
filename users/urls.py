from django.urls import path
from .views import UserLoginView, UserLogoutView, UserSignupView, UserUpdateView, UserDeleteView, UserProfileView


app_name = 'user'

urlpatterns = [
    path('signup', UserSignupView.as_view(), name='signup'),
    path('update', UserUpdateView.as_view(), name='update'),
    path('delete', UserDeleteView.as_view(), name='delete'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('profile', UserProfileView.as_view(), name='profile')
]