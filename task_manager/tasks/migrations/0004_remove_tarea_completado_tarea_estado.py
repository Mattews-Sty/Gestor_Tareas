# Generated by Django 4.2.16 on 2024-12-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_tarea_fecha_limite_tarea_completado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='completado',
        ),
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('ToDo', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], default='ToDo', max_length=10),
        ),
    ]
