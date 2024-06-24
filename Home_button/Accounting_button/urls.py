from django.urls import path
from . import views
from .views import user_list


from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accountant/', views.accountant_dashboard, name='accountant_dashboard'),
    path('director/', views.director_dashboard, name='director_dashboard'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', views.client_edit, name='client_edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('constants/', views.constant_list, name='constant_list'),  # Новый путь для редактирования констант
    path('constants/edit/<int:constant_id>/', views.constant_edit, name='constant_edit'),  # Новый путь для редактирования константы
]
