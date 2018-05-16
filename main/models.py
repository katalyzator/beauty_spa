# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class Member(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='ФИО')
    profession = models.CharField(max_length=255, verbose_name='Специализация')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    image = models.ImageField(upload_to='images/specialists', verbose_name='Картинка',
                              help_text='Размер картинки должен быть 390x300')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Спецалисты'
        verbose_name = 'Специалиста'

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Review(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    text = models.TextField(verbose_name='Текст')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')
    image = models.ImageField(upload_to='images/reviews_images', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Service(models.Model):
    SERVICE_CATEGORY = (
        ('consulting', 'Диагностика и консультация'),
        ('medicine', 'Косметология и эстетическая медицина'),
        ('spa', 'Spa терапия'),
        ('bath_spa', 'Банный spa'),
        ('art_beauty', 'Арт и Бьюти студия')
    )
    category = models.CharField(choices=SERVICE_CATEGORY, max_length=255, verbose_name='Выберите категорию')
    title = models.CharField(max_length=300, verbose_name='Название')
    description = RichTextUploadingField(verbose_name='Описание')
    # duration = models.IntegerField(default=1, verbose_name='Длительность в днях', blank=True, null=True)
    price = models.CharField(max_length=300, verbose_name='Ценообразование',
                             help_text='Пример: (от 1200 - 3000 за 1приход)')

    image = models.ImageField(upload_to='images/service_images', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услугу'

    def __unicode__(self):
        return smart_unicode(self.title)


class ServiceImage(models.Model):
    SERVICE_CATEGORY = (
        ('consulting', 'Диагностика и консультация'),
        ('medicine', 'Косметология и эстетическая медицина'),
        ('spa', 'Spa терапия'),
        ('bath_spa', 'Банный spa'),
        ('art_beauty', 'Арт и Бьюти студия')
    )

    category = models.CharField(choices=SERVICE_CATEGORY, max_length=150, verbose_name='Выберите категорию')
    image = models.ImageField(upload_to='images/service_images', verbose_name='картинка 1318x380')

    class Meta:
        verbose_name_plural = 'Фоновые картинки раздела Услуги'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.category)


class SpecialOffer(models.Model):
    SERVICE_CATEGORY = (
        ('card_club', 'Клубные карты Beauty SPA'),
        ('promotion', 'Бонусная система'),
        ('spa_party', 'Spa вечеринки'),
        ('season_offer', 'Сезонные предложения'),
    )

    category = models.CharField(choices=SERVICE_CATEGORY, max_length=150, verbose_name='Выберите категорию')
    image = models.ImageField(upload_to='images/special_offers')
    text = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Специальные предложения'
        verbose_name = 'предложения'

    def __unicode__(self):
        return smart_unicode(self.category)


class PageImage(models.Model):
    PAGE_CATEGORY = (
        ('about', 'О Нас'),
        ('gallery', 'Галерея'),
        ('etiket', 'Этикет'),
        ('news', 'События и новости'),
        ('publication', 'Публикации и пресса'),
        ('reviews', 'Отзывы'),
        ('information', 'Правовая информация'),
        ('bootick', 'Косметический Бутик'),
        ('special_offers', 'Специальные предложения'),
        ('certificates', 'СПА-Сертификаты'),
        ('kitchen', 'СПА-Кухня'),

    )

    category = models.CharField(choices=PAGE_CATEGORY, max_length=150, verbose_name='Выберите категорию')
    image = models.ImageField(upload_to='images/service_images', verbose_name='картинка 1318x380')

    class Meta:
        verbose_name_plural = 'Фоновые картинки для всех страниц'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.category)


class DiscountCertificate(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    tag = models.CharField(max_length=255, verbose_name='Тэг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Цена')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')

    image = models.ImageField(upload_to='images/certificate_images', verbose_name='Image 320x250')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Подарочные сертификаты'
        verbose_name = 'Сертификат'

    def __unicode__(self):
        return smart_unicode(self.title)


class DiscountCard(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    tag = models.CharField(max_length=255, verbose_name='Тэг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Цена')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')

    image = models.ImageField(upload_to='images/certificate_images', verbose_name='Image ')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Подарочные Карты'
        verbose_name = 'Карту'

    def __unicode__(self):
        return smart_unicode(self.title)


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = models.ImageField(upload_to='images/partners_images', verbose_name='Логотип объекта 167x52')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнера'

    def __unicode__(self):
        return smart_unicode(self.name)


class Gallery(models.Model):
    GALLERY_TYPE = (
        ('interior', 'Интерьер'),
        ('world_of_beauty', 'Мир Beauty Spa'),
        ('products', 'Продукция'),
        ('life_style', 'Стиль жизни'),
    )
    title = models.CharField(max_length=255, verbose_name='Название картинки')
    image = models.ImageField(upload_to='images/gallery_images', verbose_name='Картинка (не должно быть >1MB)')
    type_of_gallery = models.CharField(choices=GALLERY_TYPE, max_length=255, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)


class License(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название лицензии')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/license_images', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Лицензии'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)


class Slider(models.Model):
    title = models.CharField(max_length=800, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Text', blank=True, null=True)
    image = models.ImageField(upload_to='images/slider_images', verbose_name='Картинка (659x768)')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'Слайд'

    def __unicode__(self):
        return smart_unicode(self.title)


class Application(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Заявки с сайта'
        verbose_name = 'заявку'

    def __unicode__(self):
        return smart_unicode(self.first_name)


class Bootick(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/botick_images', verbose_name='Картинка')
    price = models.CharField(max_length=255, verbose_name='Цена')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Бутик'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.title)


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата проведения')
    image = models.ImageField(upload_to='images/press_images', verbose_name='Картинка')

    text = RichTextUploadingField(verbose_name='Контент события')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'

    def __unicode__(self):
        return smart_unicode(self.title)


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/press_images', verbose_name='Картинка')

    text = RichTextUploadingField(verbose_name='Контент новости')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'

    def __unicode__(self):
        return smart_unicode(self.title)


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/press_images', verbose_name='Картинка')

    text = RichTextUploadingField(verbose_name='Контент Публикации')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикацию'

    def __unicode__(self):
        return smart_unicode(self.title)


class Press(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/press_images', verbose_name='Картинка')

    text = RichTextUploadingField(verbose_name='Контент Прессы')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Пресса'
        verbose_name = 'Прессу'

    def __unicode__(self):
        return smart_unicode(self.title)


class About(models.Model):
    phone_number_1 = models.CharField(max_length=255, verbose_name='Номер телефона 1', blank=True, null=True)
    phone_number_2 = models.CharField(max_length=255, verbose_name='Номер телефона 2', blank=True, null=True)
    description = models.TextField(verbose_name='Текст', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    address = models.CharField(max_length=1000, verbose_name='Адрес', blank=True, null=True)

    facebook = models.CharField(max_length=300, verbose_name='Ссылка на facebook')
    youtube = models.CharField(max_length=300, verbose_name='Ссылка на youtube')
    instagram = models.CharField(max_length=300, verbose_name='Ссылка на instagram')

    start_time = models.TimeField(verbose_name='Время начало работы')
    end_time = models.TimeField(verbose_name='Время завершения работы')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'О Нас'
        verbose_name = 'объект'

    def __unicode__(self):
        return smart_unicode(self.phone_number_1)


class Principe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    image = models.ImageField(upload_to='images/pri_images', verbose_name='Image')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Принципы'
        verbose_name = 'принцип'

    def __unicode__(self):
        return smart_unicode(self.title)


class Promotion(models.Model):
    title = models.TextField(verbose_name='Заголовок', help_text='ТОЛЬКО В ТЕЧЕНИИ 24 ЧАСОВ')
    text = RichTextUploadingField(verbose_name='Контент Акции')

    exp_date = models.DateTimeField(verbose_name='Дата окончания', help_text='Отсчет начнется с текущей времени')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Акция'
        verbose_name = 'Акция'

    def __unicode__(self):
        return smart_unicode(self.title)


class SocialNetwork(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    link = models.CharField(max_length=300, verbose_name='Ссылка', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'объект'

    def __unicode__(self):
        return smart_unicode(self.title)
