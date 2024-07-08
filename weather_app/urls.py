from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.weather, name='weather'),
    path (staticfiles_urlpatterns())
]