from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details_view.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update_news.html'

    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def news_home(request):
    num_of_visits = request.session.get('num_os_visits', 0)
    request.session['num_of_visits'] = num_of_visits + 1
    news = News.objects.order_by('-date')
    data = {
        'news': news,
        'num_of_visits': num_of_visits
    }
    return render(request, 'news/news_home.html', data)


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Неверная форма!'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/add_news.html', data)
