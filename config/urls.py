from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Rental Demo API",
        default_version='v1',
        description="A demo API for a rental company",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hhsiju97@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', TemplateView.as_view(template_name='index.html')),

    path('api/v1/', include('products.urls')),
    path('api/v1/', include('bookings.urls')),
    path('api/v1/', include('returns.urls')),
]
