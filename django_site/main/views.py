from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Shdhd', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
