# Generated by Django 4.2.5 on 2023-09-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_habits', '0006_alter_habit_time_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_required',
            field=models.PositiveIntegerField(help_text='Time required in seconds', verbose_name='Время на выполнение'),
        ),
    ]
