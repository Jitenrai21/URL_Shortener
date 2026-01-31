from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .forms import UserRegistrationForm, URLShortenForm
from .models import ShortURL
from .utils import generate_short_key
import qrcode
import io
import base64


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
    # Get user's short URLs
    user_urls = ShortURL.objects.filter(user=request.user, is_active=True)
    return render(request, 'home.html', {'user_urls': user_urls})


@login_required
def create_short_url(request):
    """View to create a new short URL"""
    if request.method == 'POST':
        form = URLShortenForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.user = request.user
            
            # Use custom key if provided, otherwise generate one
            custom_key = form.cleaned_data.get('custom_key')
            if custom_key:
                short_url.short_key = custom_key
            else:
                short_url.short_key = generate_short_key()
            
            short_url.save()
            messages.success(request, f'Short URL created successfully! Your short key is: {short_url.short_key}')
            return redirect('url_detail', short_key=short_url.short_key)
    else:
        form = URLShortenForm()
    
    return render(request, 'shortener/create_url.html', {'form': form})


@login_required
def url_detail(request, short_key):
    """View to display details of a short URL"""
    short_url = get_object_or_404(ShortURL, short_key=short_key, user=request.user)
    
    # Build the full short URL
    full_short_url = request.build_absolute_uri(f'/{short_url.short_key}')
    
    # Generate QR code pointing to the original URL (not the short URL)
    # This allows the QR code to work on any device without needing access to the local server
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(short_url.original_url)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 for embedding in HTML
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
    qr_code_data_uri = f"data:image/png;base64,{qr_code_base64}"
    
    return render(request, 'shortener/url_detail.html', {
        'short_url': short_url,
        'full_short_url': full_short_url,
        'qr_code': qr_code_data_uri
    })


def redirect_short_url(request, short_key):
    """View to redirect from short URL to original URL"""
    try:
        short_url = get_object_or_404(ShortURL, short_key=short_key, is_active=True)
        
        # Check if URL has expired
        if short_url.is_expired():
            messages.error(request, 'This short URL has expired and is no longer available.')
            return redirect('home')
        
        # Increment click count
        short_url.increment_click()
        
        # Redirect to original URL
        return redirect(short_url.original_url)
    except Http404:
        messages.error(request, 'Short URL not found or has been deactivated.')
        return redirect('home')


@login_required
def delete_short_url(request, short_key):
    """View to delete a short URL"""
    short_url = get_object_or_404(ShortURL, short_key=short_key, user=request.user)
    
    if request.method == 'POST':
        short_url.delete()
        messages.success(request, 'Short URL deleted successfully.')
        return redirect('home')
    
    return render(request, 'shortener/delete_url.html', {'short_url': short_url})


@login_required
def edit_short_url(request, short_key):
    """View to edit a short URL"""
    short_url = get_object_or_404(ShortURL, short_key=short_key, user=request.user)
    
    if request.method == 'POST':
        form = URLShortenForm(request.POST, instance=short_url)
        if form.is_valid():
            form.save()
            messages.success(request, 'Short URL updated successfully.')
            return redirect('url_detail', short_key=short_url.short_key)
    else:
        form = URLShortenForm(instance=short_url)
    
    return render(request, 'shortener/edit_url.html', {'form': form, 'short_url': short_url})


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
