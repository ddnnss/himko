from django.shortcuts import render

def index(request):
    show_tags = True
    title = 'Главная'
    description = ''
    keywords = ''


    return render(request, 'page/index.html', locals())

