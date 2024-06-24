from django.urls import path
from . import views
from .views import user_list



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/create/', views.client_create, name='client_create'),  # Путь для создания клиента
    path('clients/delete/<int:client_id>/', views.client_delete, name='client_delete'),  # Путь для удаления клиента
    path('accountant/', views.accountant_dashboard, name='accountant_dashboard'),
    path('director/', views.director_dashboard, name='director_dashboard'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', views.client_edit, name='client_edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),  # URL для добавления пользователя
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
        # URL для удаления пользователя
   path('constants/', views.constant_list, name='constant_list'),
   path('constants/edit/<int:constant_id>/', views.constant_edit, name='constant_edit'),
]

