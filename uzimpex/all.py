from .models import *

from .forms import *


def spec(request):
    main = Banner.objects.all()
    services = Services.objects.all()
    about = About.objects.all().first()
    contact = Contacts.objects.all().first()
    form = ContactFormForm()
    form_uz = ContactForm_uz()
    form_en = ContactForm_en()

    data = {
        'main': main,
        'services': services,
        'about': about,
        'contact': contact,
        'form': form,
        'form_uz': form_uz,
        'form_en': form_en,
    }
    return data
