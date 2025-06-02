"""
URL configuration for codestar project.

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
from django.urls import path, include
from booking.views import signup  # Import signup directly


urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", signup, name="signup"),  # 🔥 Enables direct /signup/
    path('summernote/', include('django_summernote.urls')),
    path("booking/", include("booking.urls")),
    # path('booking/', include(('booking.urls', 'booking'), namespace='booking')),
    # path("", include("blog.urls"), name="blog-urls"),
    path('', include('pages.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]
