from django.db import models

from app.settings.icon import ICON

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    tema = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Newave(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 3'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Описание"

class Good(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    static = models.CharField(
        max_length=155,
        verbose_name='Статистика'
    )
    static2 = models.CharField(
        max_length=155,
        verbose_name='Статистика'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Хорошо'

class Team(models.Model):
    image = models.ImageField(
        upload_to="team/",
        verbose_name="Фото"
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    direction = models.CharField(
        max_length=100,
        verbose_name='Напрваление'
    )
    fb = models.URLField(
        verbose_name='Ссылка на фейсбук'
    )
    tw = models.URLField(
        verbose_name='Ссылка на Твитер'
    )
    gl = models.URLField(
        verbose_name='Ссылка на Гугл'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Наша команда"

class Technology(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptio = models.TextField(
        verbose_name='Описание'
    )
    icon = models.CharField(
        max_length=155,
        choices=ICON,
        verbose_name='Иконка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Технологий'