from django.contrib import admin
from django.urls import include, path

auth_patterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_patterns)),
    path('api/', include('api.urls'))
]
