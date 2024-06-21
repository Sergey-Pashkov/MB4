from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accountant/', views.accountant_dashboard, name='accountant_dashboard'),
    path('director/', views.director_dashboard, name='director_dashboard'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('clients/', views.client_list, name='client_list'),  # URL для списка клиентов
]
