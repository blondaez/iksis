from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    surname = models.CharField(max_length=25, blank=True, default='', verbose_name='Фамилия')
    name = models.CharField(max_length=25, blank=True, default='', verbose_name='Имя')
    patronymic = models.CharField(max_length=25, blank=True, default='', verbose_name='Отчество')
    phone_number = models.CharField(max_length=15, blank=True, default='', verbose_name='Номер телефона')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Service(models.Model):
    COSMETOLOGY_TYPES = [
        ('inject', 'Инъекционная косметология'),
        ('aesthetic', 'Эстетическая косметология'),
    ]

    type = models.CharField(
        max_length=50,
        choices=COSMETOLOGY_TYPES,
        verbose_name='Тип косметологии',
        default='inject'
    )
    name = models.TextField('Название события', blank=True, null=True)
    duration = models.TextField('Время проведения', blank=True, null=True)
    price = models.TextField('Цена', blank=True, null=True)
    annotation = models.TextField('Место проведения', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ProcedureRecord(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    type = models.CharField(max_length=50, verbose_name='Тип косметологии')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    date = models.DateField('Дата')
    time = models.TimeField('Время проведения')
    client_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='client_responses', verbose_name='Профиль клиента')
    response = models.BooleanField('Отклик на сободную запись', default=False)
    confirmed = models.BooleanField('Подтверждено администратором', default=False)
    active = models.BooleanField('Активна', default=False)
    completed = models.BooleanField('Выполнена', default=False)
    cancelled = models.BooleanField('Отменена', default=False)

    def save(self, *args, **kwargs):
        if self.client_profile:
            self.active = True
        if self.service:
            self.type = self.service.type
            self.price = self.service.price
        super(ProcedureRecord, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.service.name} - {self.date} {self.time}"

    class Meta:
        verbose_name = 'Запись на процедуру'
        verbose_name_plural = 'Записи на процедуры'


class Blog(models.Model):
    name = models.TextField('Название', blank=True, null=True)
    date = models.DateField('Дата публикации', blank=True, null=True)
    notes = models.TextField('Текст статьи', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='blog_images/', blank=True, null=True)
    author = models.TextField('Автор', blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.name}"

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Записи в блоге'
