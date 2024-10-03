from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_filter = ('title',)
    list_display = ('title', 'services')
    save_as_continue = True


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_filter = ('title',)
    list_display = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    save_as_continue = True


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'banner_image1')


@admin.register(Ruk)
class RukAdmin(TranslationAdmin):
    list_display = ('id', 'description')


@admin.register(Otdeli)
class OtdeliAdmin(TranslationAdmin):
    list_display = ('id', 'description')



@admin.register(Documents)
class DocumentsAdmin(TranslationAdmin):
    list_filter = ('title',)
    list_display = ('title', 'content', 'file')
    save_as_continue = True


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    list_display = ('address',)
    save_as_continue = True


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('data',)
    list_display = ('phone_number', 'data')
    save_as_continue = True


@admin.register(UsefulLinks)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    save_as_continue = True


@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    save_as_continue = True


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    save_as_continue = True
