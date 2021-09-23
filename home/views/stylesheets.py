from django.shortcuts import render


def main_style(request):
    return render(request, 'home/tooplate_style.css',
                  {}, content_type='text/css')


def gallery_style(request):
    return render(request, 'home/galleriffic-2.css',
                  {}, content_type='text/css')
