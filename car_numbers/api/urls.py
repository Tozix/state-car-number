from django.urls import include, path

from . import views

plate_patterns = [
    path('generate/', views.generate_plate),
    path('generate/<int:amount>', views.generate_plate),
    path('get/<uuid:id>', views.get_plate),
    path('add', views.add_plate)
]
urlpatterns = [
    path('plate/', include(plate_patterns)),
]
