# pages/urls.py
from django.urls import path
from . import views
app_name = "pages"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('namefood/<str:name>/', views.namefood, name="namefood"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('lotto_throw/', views.lotto_throw, name="lotto_throw"),
    path('lotto_catch/', views.lotto_catch, name="lotto_catch"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
]