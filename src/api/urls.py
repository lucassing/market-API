"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

import accounts.urls
import shop.urls

api_info = openapi.Info(
      title="Market API",
      default_version='v1',
      description="Simple and convenient market!",
      terms_of_service="https://github.com/lucassing/",
      contact=openapi.Contact(email="singlucasmartin@gmail.com"),
      license=openapi.License(name="BSD License"))


schema_view = get_schema_view(
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,))

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="marketAPI")),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('accounts/', include(accounts.urls)),
    path('shop/', include(shop.urls)),
]
