from .models import News
from django.forms import ModelForm, TextInput, DateInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'preview', 'news_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Превью новости'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'news_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
            }),
        }
