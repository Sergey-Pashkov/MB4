
# urls.py
from django.urls import path
from . import views
from .views import WorkTypeListView, WorkTypeCreateView, WorkTypeUpdateView, WorkTypeDeleteView, create_unusual_operation_log, unusual_operation_log_list, unusual_operation_log_update, unusual_operation_log_delete

from .views import (
    StandardOperationLogListView,
    StandardOperationLogCreateView,
    StandardOperationLogUpdateView,
    StandardOperationLogDeleteView
)

from .views import deviation_log_list, create_deviation_log, update_deviation_log, delete_deviation_log

from django.urls import path
from . import views
from .views import standard_operations_report 
from .views import unusual_operations_report
from .views import operations_report




urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/delete/<int:client_id>/', views.client_delete, name='client_delete'),
    path('accountant/', views.accountant_dashboard, name='accountant_dashboard'),
    path('director/', views.director_dashboard, name='director_dashboard'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', views.client_edit, name='client_edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('constants/', views.constant_list, name='constant_list'),
    path('constants/edit/<int:constant_id>/', views.constant_edit, name='constant_edit'),

    # Пути для работы с видами работ
    path('worktypes/', WorkTypeListView.as_view(), name='worktype_list'),
    path('worktypes/create/', WorkTypeCreateView.as_view(), name='worktype_create'),
    path('worktypes/update/<int:pk>/', WorkTypeUpdateView.as_view(), name='worktype_update'),
    path('worktypes/delete/<int:pk>/', WorkTypeDeleteView.as_view(), name='worktype_delete'),

    # Пути для работы с журналом нестандартных операций
    path('unusual_operation_logs/', unusual_operation_log_list, name='unusual_operation_log_list'),
    path('unusual_operation_logs/create/', create_unusual_operation_log, name='create_unusual_operation_log'),
    path('unusual_operation_logs/update/<int:pk>/', unusual_operation_log_update, name='unusual_operation_log_update'),
    path('unusual_operation_logs/delete/<int:pk>/', unusual_operation_log_delete, name='unusual_operation_log_delete'),

    # другие маршруты...
    path('standard_operation_logs/', StandardOperationLogListView.as_view(), name='standard_operation_log_list'),
    path('standard_operation_logs/create/', StandardOperationLogCreateView.as_view(), name='standard_operation_log_create'),
    path('standard_operation_logs/update/<int:pk>/', StandardOperationLogUpdateView.as_view(), name='standard_operation_log_update'),
    path('standard_operation_logs/delete/<int:pk>/', StandardOperationLogDeleteView.as_view(), name='standard_operation_log_delete'),

    path('deviation_logs/', views.deviation_log_list, name='deviation_log_list'),
    path('deviation_logs/create/', views.create_deviation_log, name='create_deviation_log'),
    path('deviation_logs/<int:pk>/edit/', views.update_deviation_log, name='update_deviation_log'),
    path('deviation_logs/<int:pk>/delete/', views.delete_deviation_log, name='delete_deviation_log'),

    # другие пути
    path('standard_operations_report/', standard_operations_report, name='standard_operations_report'),

    # ... другие пути ...
    path('unusual_operations_report/', unusual_operations_report, name='unusual_operations_report'),

    # другие пути
    path('operations_report/', operations_report, name='operations_report'),

    # ... другие маршруты ...
    path('api/worktype-cost/<int:pk>/', views.worktype_cost, name='worktype_cost'),
]
