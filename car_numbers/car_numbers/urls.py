from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('jwt/', include(jwt_patterns)),
    path('api/', include('api.urls'))
]
