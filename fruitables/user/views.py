from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        authenticated_user = authenticate(
            email=user.email,
            password=form.cleaned_data['password1'],
            backend='user.backends.EmailBackend'
        )

        login(self.request, authenticated_user)
        return response

class LogInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    next_page = reverse_lazy('home')


