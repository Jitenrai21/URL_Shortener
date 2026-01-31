"""
URL configuration for url_shortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shortenerApp.views import (
    register, home, CustomLoginView, CustomLogoutView,
    create_short_url, url_detail, redirect_short_url,
    delete_short_url, edit_short_url
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    
    # URL shortener routes
    path("shorten/", create_short_url, name="create_short_url"),
    path("url/<str:short_key>/", url_detail, name="url_detail"),
    path("url/<str:short_key>/edit/", edit_short_url, name="edit_short_url"),
    path("url/<str:short_key>/delete/", delete_short_url, name="delete_short_url"),
    
    # Redirect route - must be last
    path("<str:short_key>/", redirect_short_url, name="redirect_short_url"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
