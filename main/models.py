from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class AdvUser(AbstractUser):
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещение о новых коментариях?')
    test_field = models.BooleanField(default=True, verbose_name='Тестовое поле')

    class Meta(AbstractUser.Meta):
        pass


class Review(models.Model):
    name = models.CharField('Имя', max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=uuid.uuid1)
    age = models.PositiveIntegerField('Возраст', blank=True, null=True)
    image = models.ImageField(upload_to='main/static/avatar/%Y/%m/%d', blank=True, help_text='Добавить фото')
    email = models.EmailField(max_length=254, blank=True, null=True)
    tel = models.CharField('Номер телефона', max_length=17, blank=True, null=True)
    review = models.TextField('Отзыв', max_length=1500)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    done = models.BooleanField('Активация', default=False)


    class Meta:
        ordering = ('created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField('Название парикмахерской', max_length=600, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=uuid.uuid1)
    address = models.CharField('Адресс', max_length=600)
    tel = models.CharField('Номер телефона', max_length=20, blank=True, null=True)
    social = models.CharField('социальные сети', max_length=600)
    email = models.EmailField(max_length=254, blank=True, null=True)
    contact = models.TextField('О Нас', max_length=1500, blank=True)
    image = models.ImageField(upload_to='main/static/contacts/%Y/%m/%d', blank=True, help_text='Добавить фото')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField('Ваше имя', max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=uuid.uuid1)
    tel = models.CharField('Номер телефона', max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    theme = models.CharField('Тема вопроса', max_length=300, blank=True, null=True)
    contact = models.TextField('Напишите свой вопрос', max_length=1500, blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField('Название скидки', max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=uuid.uuid1)
    percentage = models.DecimalField('% скидки', max_digits=3, decimal_places=0, blank=True, null=True)
    word = models.CharField('Условие акции', max_length=254)
    comment = models.CharField('Примечание', max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='main/static/contacts/%Y/%m/%d', blank=True, help_text='Добавить фото')
    tag = models.CharField(max_length=50)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name


class Masters(models.Model):
    name = models.CharField('Имя мастера', max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=uuid.uuid1)
    comment = models.TextField('Описание', max_length=2000, blank=True, null=True)
    tag = models.CharField('master_1 или master_2', max_length=50)
    photo1 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', help_text='Добавить фото')
    diploma1 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Добавить Диплом')
    diploma2 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Добавить Диплом')
    diploma3 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Добавить Диплом')
    diploma4 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Добавить Диплом')
    example1 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Примеры работ')
    example2 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Примеры работ')
    example3 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Примеры работ')
    example4 = models.ImageField(upload_to='main/static/masters/%Y/%m/%d', blank=True, help_text='Примеры работ')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name

