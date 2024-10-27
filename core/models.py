from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import admin

class EmployeeManager(BaseUserManager):
    def create_user(self, email, name, position, pay_rate, phone_number, password=None):
        if not email:
            raise ValueError("Employees must have an email address")
        email = self.normalize_email(email)
        employee = self.model(email=email, name=name, position=position, pay_rate=pay_rate, phone_number=phone_number)
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, email, name, position, pay_rate, phone_number, password=None):
        employee = self.create_user(email, name, position, pay_rate, phone_number, password)
        employee.is_superuser = True
        employee.is_staff = True
        employee.save(using=self._db)
        return employee

class Employee(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('superAdmin', 'Super Admin'),
        ('staff', 'Staff')
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'position', 'pay_rate', 'phone_number']

    objects = EmployeeManager()

    def __str__(self):
        return self.name

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'role', 'pay_rate', 'is_staff', 'is_superuser')
    search_fields = ('name', 'email', 'position')

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    search_fields = ('name',)

class ClockRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='clock_records')
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Clock record for {self.employee.name}"

@admin.register(ClockRecord)
class ClockRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'clock_in', 'clock_out')
    list_filter = ('employee',)

class HolidayRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='holiday_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.status} ({self.start_date} to {self.end_date})"

@admin.register(HolidayRequest)
class HolidayRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'employee')

class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High')
    ]

    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'assigned_to', 'priority', 'status', 'due_date')
    list_filter = ('status', 'priority', 'assigned_to')
    search_fields = ('text', 'assigned_to__name')
