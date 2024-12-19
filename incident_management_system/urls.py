"""
URL configuration for incident_management_system project.

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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views
# Define the Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Incident Management System API",
        default_version='v1',
        description="API documentation for the incident management system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@incidentmanagement.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/', include('incidents.urls')),
    path('auth/', include('djoser.urls')),  # Login and Password Reset
    path('auth/', include('djoser.urls.authtoken')),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    # Redoc UI (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
