from django.shortcuts import render


def about(request):
    current_menu = 'about'
    page_id = 'subpage'
    header_id = 'tooplate_header_sp'
    title = 'Информация'
    return render(request, 'home/about.html', locals())
