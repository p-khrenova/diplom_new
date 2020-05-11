from django.db import models
from django import forms

from django.contrib.auth.models import User, AbstractUser


class Master (models.Model):
    profile_img = models.ImageField(upload_to='img/users/', blank=True, null=True)
    name=models.CharField(verbose_name='ФИО', max_length = 300 )
    specialization=models.CharField(verbose_name='Специализация',max_length=300)
    info=models.CharField(verbose_name='Инфо о мастере',max_length=10000)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Мастера"
        verbose_name = "Мастер"

class MasterUsl(models.Model):
    master = models.ForeignKey(Master, verbose_name='Услуги')
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    price = models.CharField(verbose_name='Стоимость услуги', max_length=100)
    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Услуги"
        verbose_name = "Услуга"


class Stock(models.Model):
    nameStock = models.CharField(verbose_name='Название акции', max_length=200)
    price = models.CharField(verbose_name='Стоимость', max_length=200)
    info = models.CharField(verbose_name='Описание акции', max_length=500)
    def __str__(self):
        return '%s ' % self.nameStock

    class Meta:
        verbose_name_plural = "Акции"
        verbose_name = "Акция"

class ContactsForm(models.Model):
    person = models.CharField(verbose_name='ФИО', max_length=222)
    mail = models.EmailField(verbose_name='Email', max_length=200)
    message = models.CharField(verbose_name='Сообщение', max_length=400)
    def __str__(self):
        return '%s ' % self.person

    class Meta:
        verbose_name_plural = "Формы"
        verbose_name = "Форма"


class StockReserv(models.Model):
    persons = models.CharField(verbose_name='ФИО', max_length=221)
    phone = models.CharField(verbose_name='Телефон', max_length=200)
    mail = models.EmailField(verbose_name='Email', max_length=200)
    stockId = models.ForeignKey(Stock, verbose_name='Акция')
    def __str__(self):
        return self.persons

    class Meta:
        verbose_name_plural = "Акционные записи"
        verbose_name = "Акции"

class Reception(models.Model):
    date = models.DateField(verbose_name='Дата приема ')
    time=models.CharField(verbose_name='Время приема ', max_length=5)
    client_name=models.CharField(verbose_name='ФИО ', max_length=300)
    client_info=models.CharField(verbose_name='Инфо о клиенте ', max_length=10000)
    master=models.ForeignKey(Master, verbose_name='Мастер ',)
    uslugi=models.ForeignKey(MasterUsl, verbose_name='Услуги ',)
    cost = models.CharField( verbose_name='Стоимость услуг',max_length=100,)
    person_id = models.ForeignKey(User, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"

class Human(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя")
    surname = models.CharField(max_length=60, verbose_name="Фамилия")

    def __str__(self):
        return 'Имя - {0}, Фамилия - {1}'.format(self.name, self.surname)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='img/users/', default='img/users/1.jpg', verbose_name='Изображение')
    phone = models.CharField(max_length=200, default='+7', verbose_name='Номер телефона')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


