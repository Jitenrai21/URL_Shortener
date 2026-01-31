from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    """Admin interface for ShortURL model"""
    list_display = ['short_key', 'original_url', 'user', 'click_count', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at', 'user']
    search_fields = ['short_key', 'original_url', 'user__username']
    readonly_fields = ['created_at', 'click_count']
    ordering = ['-created_at']
