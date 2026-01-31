from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    """Home page view - requires authentication"""
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    """Custom login view with additional functionality"""
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Login successful!')
        return super().get_success_url()


class CustomLogoutView(LogoutView):
    """Custom logout view"""
    next_page = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have been logged out successfully.')
        return super().dispatch(request, *args, **kwargs)
