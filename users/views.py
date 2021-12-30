from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationForm, UserUpdateForm
from .models import User

class UserSignupView(View):
    model = User
    form = UserCreationForm
    template_name = 'users/signup.html'
    success_url = 'profile'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if username and password1 and password2 \
                and password1 == password2:

                user = User.objects.create_user(
                    username = username,
                    password = password1
                )
                user.save()
                login(request, user)

                if user:
                    return HttpResponseRedirect(self.success_url)
        context = {
            'form': form,
            'error': 'Usuário ou senha inválido'
        }
        return render(request, self.template_name, context)

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, self.template_name, context)

class UserUpdateView(LoginRequiredMixin, View):
    model = User
    form = UserUpdateForm
    template_name = 'users/update.html'
    success_url = 'profile'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            context = { 'error': 'erro ao tentar atualizar o perfil'}
            return render(request, self.template_name, context)

class UserDeleteView(LoginRequiredMixin, View):
    model = User
    template_name = 'users/confirm_delete.html'
    safeword = 'DELETE'
    success_url = '/'

    def get(self, request):
        context = {
            'user': request.user,
            'safeword': self.safeword
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get('safeword') == self.safeword:
            request.user.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            context = {
                'error': 'A palavra de segurança não está correta',
                'safeword': self.safeword
            }
            return render(request, self.template_name, context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = '/'

class UserLogoutView(LogoutView):
    next_page = '/'
