from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class ShortURL(models.Model):
    """Model to store shortened URLs"""
    original_url = models.URLField(max_length=2048, help_text="The original long URL")
    short_key = models.CharField(max_length=10, unique=True, db_index=True, help_text="The unique short key")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='short_urls')
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True, help_text="Optional expiration date and time")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"
    
    def __str__(self):
        return f"{self.short_key} -> {self.original_url}"
    
    def get_short_url(self):
        """Return the full short URL"""
        return f"{self.short_key}"
    
    def increment_click(self):
        """Increment the click count"""
        self.click_count += 1
        self.save(update_fields=['click_count'])
    
    def is_expired(self):
        """Check if the short URL has expired"""
        if self.expires_at is None:
            return False
        return timezone.now() > self.expires_at
