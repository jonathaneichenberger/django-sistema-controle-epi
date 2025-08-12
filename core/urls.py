from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('epis/', views.listar_epis, name='listar_epis'),
    path('usuarios/', views.usuarios, name='usuarios'),     
    path('entregas/', views.entregas, name='entregas'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
