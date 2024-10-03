from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description2')


@register(Otdeli)
class OtdeliTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Ruk)
class RukTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Documents)
class DocumentsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('address',)
