from .models import *
from django import forms


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['phone_number', ]
        widgets = {
            'phone_number': forms.TextInput(
                attrs={'type': "number", "autocomplete": "off", "placeholder": "Например: +998 (99) 123-45-67",
                       'class': 'text-input contact__input', "maxlength": "15", 'required': ' '}),

        }


class ContactForm_uz(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['phone_number', ]
        widgets = {
            'phone_number': forms.TextInput(
                attrs={'type': "number", "autocomplete": "off", "placeholder": "Masalan: +998 (99) 123-45-67",
                       'class': 'text-input contact__input', "maxlength": "15", 'required': ' '}),

        }


class ContactForm_en(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['phone_number', ]
        widgets = {
            'phone_number': forms.TextInput(
                attrs={'type': "number", "autocomplete": "off", "placeholder": "For Example: +998 (99) 123-45-67",
                       'class': 'text-input contact__input', "maxlength": "15", 'required': ' '}),

        }
