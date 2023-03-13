from django.urls import include, path
from django.contrib import admin
from rest_framework.schemas import get_schema_view

from .api import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path(
        "openapi",
        get_schema_view(title="Food Saver API", description="API", version="1.0.0"),
        name="openapi-schema",
    ),
    ]
