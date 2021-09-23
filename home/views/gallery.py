from django.shortcuts import render


def gallery(request):
    current_menu = 'gallery'
    page_id = 'subpage'
    header_id = 'tooplate_header_sp'
    title = 'Галерея'
    return render(request, 'home/gallery.html', locals())
