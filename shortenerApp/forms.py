from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ShortURL


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class URLShortenForm(forms.ModelForm):
    """Form for creating short URLs"""
    original_url = forms.URLField(
        max_length=2048,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your long URL here...',
            'required': True
        }),
        label='Long URL'
    )
    custom_key = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Custom short key (optional)',
        }),
        label='Custom Short Key (Optional)',
        help_text='Leave blank for auto-generated key. Only letters, numbers allowed.'
    )
    
    class Meta:
        model = ShortURL
        fields = ['original_url']
    
    def clean_custom_key(self):
        """Validate custom key"""
        custom_key = self.cleaned_data.get('custom_key', '').strip()
        
        if custom_key:
            # Check if key contains only alphanumeric characters
            if not custom_key.isalnum():
                raise forms.ValidationError('Custom key can only contain letters and numbers.')
            
            # Check if key already exists
            if ShortURL.objects.filter(short_key=custom_key).exists():
                raise forms.ValidationError('This custom key is already taken. Please choose another.')
        
        return custom_key