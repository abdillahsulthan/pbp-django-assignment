# Generated by Django 4.1 on 2022-09-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_rename_status_task_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_finished',
            field=models.TextField(default='Belum'),
        ),
    ]
