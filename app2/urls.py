from django.urls import path
from . import views

# aca si se agregan todas las ulr de la app
urlpatterns = [
    path('', views.intento2),
    path('22/',views.vista2),
]
