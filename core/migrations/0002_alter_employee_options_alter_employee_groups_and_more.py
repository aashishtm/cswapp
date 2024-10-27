# Generated by Django 5.1.2 on 2024-10-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_edit_employee', 'Can edit employee'),)},
        ),
        migrations.AlterField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_employee_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_employee_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
