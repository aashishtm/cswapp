from django.urls import path
from . import views

urlpatterns = [
    # Login view
    path('login/', views.login_view, name='login'),

    # Dashboard views
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # Employee views
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Inventory views
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/create/', views.inventory_create, name='inventory_create'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),

    # Task views
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Clock record views
    path('clock_records/', views.clock_record_list, name='clock_record_list'),
    path('clock_records/create/', views.clock_record_create, name='clock_record_create'),
    path('clock_records/<int:pk>/edit/', views.clock_record_edit, name='clock_record_edit'),
    path('clock_records/<int:pk>/delete/', views.clock_record_delete, name='clock_record_delete'),

    # Holiday request views
    path('holiday_requests/', views.holiday_request_list, name='holiday_request_list'),
    path('holiday_requests/create/', views.holiday_request_create, name='holiday_request_create'),
    path('holiday_requests/<int:pk>/edit/', views.holiday_request_edit, name='holiday_request_edit'),
    path('holiday_requests/<int:pk>/delete/', views.holiday_request_delete, name='holiday_request_delete'),

    # Work hours view (to fix NoReverseMatch error)
    path('work_hours/', views.work_hours_list, name='work_hours_list'),

    # Logout view
    path('logout/', views.logout_view, name='logout'),
]
