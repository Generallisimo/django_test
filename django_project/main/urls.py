from django.urls import path
from . import views
urlpatterns = [
    # вызываем фун из этого файла и даем им названия 
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
]
