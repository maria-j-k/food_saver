from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .api import router

yasg_schema_view = get_schema_view(
    openapi.Info(
        title="Food Saver API",
        default_version="v1",
        description="App to manage your food shopping and cooking",
        #   terms_of_service="https://www.google.com/policies/terms/",
        #   contact=openapi.Contact(email="contact@snippets.local"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("swagger.json/", yasg_schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", yasg_schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", yasg_schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
