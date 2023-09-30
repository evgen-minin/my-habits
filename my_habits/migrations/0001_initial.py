# Generated by Django 4.2.5 on 2023-09-30 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('place', models.CharField(max_length=255, verbose_name='Место')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время')),
                ('action', models.TextField(verbose_name='Действие')),
                ('is_reward', models.BooleanField(blank=True, null=True, verbose_name='Признак приятной привычки')),
                ('frequency', models.PositiveIntegerField(default=1, help_text='Frequency in days', verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознаграждение')),
                ('time_required_new', models.PositiveIntegerField(blank=True, help_text='Time required', null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(blank=True, null=True, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, limit_choices_to={'is_reward': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
