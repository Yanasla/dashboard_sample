from django.shortcuts import render


def blog(request):
    current_menu = 'blog'
    page_id = 'subpage'
    header_id = 'tooplate_header_sp'
    title = 'Блог'
    return render(request, 'home/blog.html', locals())
