from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

auth_patterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_patterns)),
    path('api/', include('api.urls'))
]

schema_view = get_schema_view(
    openapi.Info(
        title="State car number API",
        default_version='v1',
        description="Документация для проекта State car number",
        contact=openapi.Contact(email="tozix@yandex.ru"),
        license=openapi.License(name="BSD 2-Clause License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
