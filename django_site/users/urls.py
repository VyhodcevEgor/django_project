from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('<int:uid>', views.profile, name='profile')
]
