from django.shortcuts import render


def contact(request):
    current_menu = 'contact'
    page_id = 'subpage'
    header_id = 'tooplate_header_sp'
    title = 'Контакт'
    return render(request, 'home/contact.html', locals())
