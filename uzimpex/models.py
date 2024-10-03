from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Services(models.Model):
    banner = models.ImageField(verbose_name='Banner', upload_to='about/', blank=True, null=True)
    banner1 = models.ImageField(verbose_name='Banner1', upload_to='about/', blank=True, null=True)
    banner2 = models.ImageField(verbose_name='Banner2', upload_to='about/', blank=True, null=True)
    banner3 = models.ImageField(verbose_name='Banner3', upload_to='about/', blank=True, null=True)
    banner4 = models.ImageField(verbose_name='Banner4', upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=2000, verbose_name='Service Title ')
    description = RichTextField(verbose_name='Text')
    slug = models.SlugField(verbose_name='Slug', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервисы'


class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Slider name')
    services = models.ForeignKey(Services, related_name='serv', blank=True, on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name='Main image', upload_to='banner/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'


class About(models.Model):
    banner_image1 = models.ImageField(verbose_name='Banner1', upload_to='about/', null=True, blank=True, )
    banner_image2 = models.ImageField(verbose_name='Banner2', upload_to='about/', null=True, blank=True, )
    title = models.CharField(max_length=2000, verbose_name='About title ')
    description = RichTextField()
    description2 = RichTextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О Компании'
        verbose_name_plural = 'О Компании'


class Ruk(models.Model):
    description = RichTextUploadingField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'


class Otdeli(models.Model):
    description = RichTextUploadingField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Отделы'
        verbose_name_plural = 'Отделы'


class Documents(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Slider name')
    content = RichTextUploadingField(verbose_name='Slider description')
    file = models.FileField(verbose_name='Main file', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'


class Contacts(models.Model):
    phone = models.CharField(max_length=200, verbose_name='Phone number2 ')
    email = models.CharField(max_length=200, verbose_name='Email ')
    address = models.CharField(max_length=200, verbose_name='Address ')
    telegram = models.CharField(max_length=200, verbose_name='Telegram ')
    instagram = models.CharField(max_length=200, verbose_name='Instagram ')
    youtube = models.CharField(max_length=200, verbose_name='Youtube ')
    map = models.CharField(max_length=10000, verbose_name="Карта", null=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class ContactForm(models.Model):
    phone_number = models.CharField(max_length=200, verbose_name='Phone_number')
    data = models.DateTimeField(auto_created=True, default=datetime.datetime.now(), verbose_name='Получено', null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Контактная форма'
        verbose_name_plural = 'Контактная форма'


class UsefulLinks(models.Model):
    name = models.CharField(blank=True, max_length=100)
    image = models.ImageField(verbose_name='Useful links', upload_to='logo/', null=True)
    link = models.URLField()

    def __str__(self):
        return f'Image- {self.id}'

    class Meta:
        verbose_name = 'Партнёры'
        verbose_name_plural = 'Партнёры'


class Links(models.Model):
    name = models.CharField(blank=True, max_length=100)
    image = models.ImageField(verbose_name='Useful links', upload_to='logo/', null=True)
    link = models.URLField()

    def __str__(self):
        return f'Image- {self.id}'

    class Meta:
        verbose_name = 'Полезные ссылки'
        verbose_name_plural = 'Полезные ссылки'


class HomeVideo(models.Model):
    name = models.CharField(max_length=128, default='Home Video')
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.name or None

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
