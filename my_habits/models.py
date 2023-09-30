from django.core.exceptions import ValidationError
from django.db import models
from users.models import User


class Habit(models.Model):
    """
    Модель, описывающая привычку пользователя.

    Поля:
    - user (ForeignKey): Пользователь, создавший привычку.
    - title (CharField): Заголовок привычки.
    - place (CharField): Место, где необходимо выполнять привычку.
    - time (TimeField): Время, когда необходимо выполнять привычку.
    - action (TextField): Действие, которое представляет из себя привычку.
    - is_reward (BooleanField): Признак приятной привычки.
    - related_habit (ForeignKey, optional): Связанная привычка, если есть. Ограничена на выбор приятных привычек.
    - frequency (PositiveIntegerField): Периодичность выполнения привычки для напоминания в днях.
    - reward (CharField): Вознаграждение за выполнение привычки.
    - time_required (PositiveIntegerField): Время, которое предположительно потратит пользователь на выполнение привычки в секундах.
    - is_public (BooleanField): Признак публичности привычки.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(null=True, blank=True, verbose_name="Время")
    action = models.TextField(verbose_name="Действие")
    is_reward = models.BooleanField(verbose_name="Признак приятной привычки", null=True, blank=True)
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                      limit_choices_to={'is_reward': True}, verbose_name="Связанная привычка")
    frequency = models.PositiveIntegerField(default=1, help_text="Frequency in days", verbose_name="Периодичность")
    reward = models.CharField(max_length=255, verbose_name="Вознаграждение", null=True, blank=True)
    time_required_new = models.PositiveIntegerField(help_text='Time required', null=True, blank=True,
                                         verbose_name="Время на выполнение")
    is_public = models.BooleanField(verbose_name="Признак публичности", null=True, blank=True)

    def clean(self):
        """
        Метод для валидации полей модели.

        Проверяет различные условия, чтобы убедиться, что данные валидны.
        Генерирует ValidationError в случае нарушения условий.
        """
        if self.related_habit and self.is_reward:
            raise ValidationError("Нельзя одновременно выбирать связанную привычку и указывать вознаграждение.")

        if self.time_required_new > 120:
            raise ValidationError("Время выполнения не может быть больше 120 секунд.")

        if self.related_habit and not self.related_habit.is_reward:
            raise ValidationError("Связанная привычка должна быть приятной привычкой.")

        if self.is_reward:
            if self.related_habit:
                raise ValidationError("Приятная привычка не может иметь связанную привычку.")
            if self.reward:
                raise ValidationError("Приятная привычка не может иметь вознаграждение.")

        if self.frequency < 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
