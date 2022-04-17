from django.db import models


class Gardens(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип сада')
    age = models.CharField(max_length=15, verbose_name='Возрост от')
    time = models.CharField(max_length=30,  blank=True, null=True, verbose_name='Время с по ')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price_for_one = models.FloatField(null=True, blank=True, verbose_name='Цена за одно занятие')
    price_for_month = models.FloatField(null=True, blank=True, verbose_name='Цена за месяц')
    types = models.ManyToManyField('Schedule', related_name='type')
    poster = models.ImageField("Постер", blank=True, upload_to="posters")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Тип сада'
        verbose_name = 'Типы садов'
        # ordering = ['published']


class Schedule(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип расписания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Расписание'
        verbose_name = 'Расписания'
