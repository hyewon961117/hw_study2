# 내장함수 url import
from address import views
from django.urls import path

urlpatterns = [
    # http://localhost:80/address/***
    # ***가 write 이면 views.write으로
    path('', views.home),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]