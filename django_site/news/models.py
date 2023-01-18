from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    preview = models.CharField('Превью', max_length=250)
    news_text = models.TextField('Текст новости')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField('Автор комментария', max_length=40)
    comment_text = models.CharField('Текст комментария', max_length=250)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

