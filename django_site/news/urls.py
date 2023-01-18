from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.add_news, name='add_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path(
        '<int:pk>/update',
        views.NewsUpdateView.as_view(),
        name='news_update'
    ),
    path(
        '<int:pk>/delete',
        views.NewsDeleteView.as_view(),
        name='news_delete'
    ),
    path(
        '<int:pk>/leave_comment/',
        views.leave_comment,
        name='leave_comment'
    ),
]
