# Generated by Django 4.1 on 2022-09-27 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_status_alter_task_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='is_finished',
        ),
    ]
