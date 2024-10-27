# core/forms.py
from django import forms
from .models import Employee, InventoryItem, HolidayRequest, ClockRecord, Task

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'pay_rate', 'email', 'phone_number', 'role']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full Name'}),
            'position': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Position'}),
            'pay_rate': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Pay Rate'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'role': forms.Select(attrs={'class': 'form-select'})
        }

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Item Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Quantity'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Price'}),
        }

class HolidayRequestForm(forms.ModelForm):
    class Meta:
        model = HolidayRequest
        fields = ['employee', 'start_date', 'end_date', 'status', 'reason']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'reason': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Reason for Request'}),
        }

class ClockRecordForm(forms.ModelForm):
    class Meta:
        model = ClockRecord
        fields = ['employee', 'clock_in', 'clock_out']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'clock_in': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'clock_out': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'completed', 'due_date', 'assigned_to', 'priority', 'status', 'description']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Task Description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'due_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Priority'}),
            'status': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Status'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Task Description'}),
        }