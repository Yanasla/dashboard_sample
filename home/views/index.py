from django.shortcuts import render


def index(request):
    current_menu = 'home'
    page_id = 'home'
    header_id = 'tooplate_header'
    title = 'Python, Django, PostgreSQL'
    return render(request, 'home/index.html', locals())
