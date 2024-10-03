from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages

from .forms import *
import telebot

token = "7261556871:AAH7kkSsAxa9Iibu3Vy_dfjo20KPMlKoTjM"
bot = telebot.TeleBot(token)
admin_id = 114253636


def index(request):
    main = Banner.objects.all()
    services = Services.objects.all()
    about = About.objects.all().first()
    contact = Contacts.objects.all().first()
    useful_links = UsefulLinks.objects.all()
    form = ContactFormForm()
    links = Links.objects.all()
    video_obj = HomeVideo.objects.all().first()

    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение принято. Скоро свяжемся!!!')
            # message_name = request.POST['name']
            message_phone = request.POST['phone_number']
            # message_email = request.POST['email']
            # message_text = request.POST['message']
            sms = f'📩 Вам пришло сообщение \n\n☎️ Номер телефона: +{message_phone}\n'
            bot.send_message(admin_id, sms)
            redirect('index')
        else:
            form = ContactForm()

    data = {
        'main': main,
        'services': services,
        'about': about,
        'contact': contact,
        'form': form,
        'useful_links': useful_links,
        'links': links,
        'video_obj': video_obj,
    }
    return render(request, 'index.html', data)


def message_uz(request):
    form_uz = ContactForm_uz()
    if request.method == 'POST':
        form_uz = ContactForm_uz(request.POST)
        if form_uz.is_valid():
            form_uz.save()
            messages.success(request, 'Sizning xabaringiz qabul qilindi. Tez orada aloqaga chiqamiz!!!')
            message_phone = request.POST['phone_number']
            sms = f'📩 Sizga xabar keldi\n\n☎️ Telefon raqami: +{message_phone}\n'

            bot.send_message(admin_id, sms)
            redirect('index')
    data = {
        'form_uz': form_uz,
    }
    return render(request, 'main/services.html', data)


def message_en(request):
    form_en = ContactForm_en()
    if request.method == 'POST':
        form_en = ContactForm_en(request.POST)
        if form_en.is_valid():
            form_en.save()
            messages.success(request, 'Sizning xabaringiz qabul qilindi. Tez orada aloqaga chiqamiz!!!')
            message_phone = request.POST['phone_number']
            sms = f'📩 Sizga xabar keldi\n\n☎️ Telefon raqami: +{message_phone}\n'
            bot.send_message(admin_id, sms)
            return redirect('index')
    data = {
        'form_en': form_en,
    }
    return render(request, 'main/services.html', data)


def services(request):
    services = Services.objects.all()
    data = {
        'services': services
    }
    return render(request, 'main/services.html', data)


def services_detail(request, slug):
    services_detail = Services.objects.get(slug=slug)
    data = {
        'services_detail': services_detail
    }
    return render(request, 'main/servicesPage.html', data)


def documents(request):
    documents = Documents.objects.all()
    data = {
        'documents': documents
    }
    return render(request, 'main/documents.html', data)


def contacts(request):
    contact = Contacts.objects.all().first()
    form = ContactFormForm()

    data = {
        'contact': contact,
        'form': form,
        # 'form_uz':form_uz
    }
    return render(request, 'main/contact.html', data)


def about(request):
    about = About.objects.all().first()
    data = {
        'about': about
    }
    return render(request, 'main/about.html', data)


def department(request):
    department = Otdeli.objects.all().first()
    data = {
        'department': department
    }
    return render(request, 'main/department.html', data)


def ruk(request):
    ruk = Ruk.objects.all().first()
    data = {
        'ruk': ruk
    }
    return render(request, 'main/ruk.html', data)


def useful_links(request):
    useful_links = UsefulLinks.objects.all()
    data = {
        'useful_links': useful_links
    }
    return render(request, 'main/useful_links.html', data)


def page_not_found_view_404(request, exception):
    return render(request, "errors/404.html", {}, status=404)


def server_error_view_500(request):
    return render(request, "errors/500.html", status=500)


def bad_request_view_400(request, exception):
    return render(request, "errors/400.html", status=400)
