# Generated by Django 4.1.5 on 2023-01-12 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=40, verbose_name='Автор комментария')),
                ('comment_text', models.CharField(max_length=250, verbose_name='Текст комментария')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
