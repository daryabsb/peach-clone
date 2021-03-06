"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core.views import Home, testjs

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("accounts/", include("users.urls", namespace="users")),
    path("", Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path("companies/", include("company.urls", namespace="companies")),
    path("transactions/", include("transactions.urls", namespace="transactions")),
    path("statements/", include("statement.urls", namespace="statements")),
    path("testjs/", testjs),
    
    path('sales/',include('sales.urls')),
    path('purchases/',include('purchase.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
