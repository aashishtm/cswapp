from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee, InventoryItem, Task, ClockRecord, HolidayRequest
from .forms import EmployeeForm, InventoryItemForm, TaskForm, ClockRecordForm, HolidayRequestForm

# Login View
def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard' if user.role == 'superAdmin' else 'employee_dashboard')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid form submission. Please check your inputs."
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form, 'error': error_message})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard Views
@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def employee_dashboard(request):
    return render(request, 'core/employee_dashboard.html')

# Helper function for handling form creation and editing
def handle_form(request, form_class, template_name, redirect_name, instance=None):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_name)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {'form': form})

# Employee Views
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    return handle_form(request, EmployeeForm, 'core/employee_form.html', 'employee_list')

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return handle_form(request, EmployeeForm, 'core/employee_form.html', 'employee_list', employee)

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'core/employee_confirm_delete.html', {'employee': employee})

# Inventory Views
@login_required
def inventory_list(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'core/inventory_list.html', {'inventory_items': inventory_items})

@login_required
def inventory_create(request):
    return handle_form(request, InventoryItemForm, 'core/inventory_form.html', 'inventory_list')

@login_required
def inventory_edit(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    return handle_form(request, InventoryItemForm, 'core/inventory_form.html', 'inventory_list', inventory_item)

@login_required
def inventory_delete(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')
    return render(request, 'core/inventory_confirm_delete.html', {'inventory_item': inventory_item})

# Task Views
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'core/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    return handle_form(request, TaskForm, 'core/task_form.html', 'task_list')

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return handle_form(request, TaskForm, 'core/task_form.html', 'task_list', task)

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'core/task_confirm_delete.html', {'task': task})

# Clock Record Views
@login_required
def clock_record_list(request):
    clock_records = ClockRecord.objects.all()
    return render(request, 'core/clock_record_list.html', {'clock_records': clock_records})

@login_required
def clock_record_create(request):
    return handle_form(request, ClockRecordForm, 'core/clock_record_form.html', 'clock_record_list')

@login_required
def clock_record_edit(request, pk):
    clock_record = get_object_or_404(ClockRecord, pk=pk)
    return handle_form(request, ClockRecordForm, 'core/clock_record_form.html', 'clock_record_list', clock_record)

@login_required
def clock_record_delete(request, pk):
    clock_record = get_object_or_404(ClockRecord, pk=pk)
    if request.method == 'POST':
        clock_record.delete()
        return redirect('clock_record_list')
    return render(request, 'core/clock_record_confirm_delete.html', {'clock_record': clock_record})

# Holiday Request Views
@login_required
def holiday_request_list(request):
    holiday_requests = HolidayRequest.objects.all()
    return render(request, 'core/holiday_request_list.html', {'holiday_requests': holiday_requests})

@login_required
def holiday_request_create(request):
    return handle_form(request, HolidayRequestForm, 'core/holiday_request_form.html', 'holiday_request_list')

@login_required
def holiday_request_edit(request, pk):
    holiday_request = get_object_or_404(HolidayRequest, pk=pk)
    return handle_form(request, HolidayRequestForm, 'core/holiday_request_form.html', 'holiday_request_list', holiday_request)

@login_required
def holiday_request_delete(request, pk):
    holiday_request = get_object_or_404(HolidayRequest, pk=pk)
    if request.method == 'POST':
        holiday_request.delete()
        return redirect('holiday_request_list')
    return render(request, 'core/holiday_request_confirm_delete.html', {'holiday_request': holiday_request})

# Work Hours List View (New View to Fix NoReverseMatch)
@login_required
def work_hours_list(request):
    # Sample context data; replace with actual data logic if necessary
    work_hours = ClockRecord.objects.all()  # Assuming work hours are stored in ClockRecord
    return render(request, 'core/work_hours_list.html', {'work_hours': work_hours})
