from django.contrib import admin
from django.urls import path, include
from config import views

urlpatterns = [
    # 관리자용 사이트
    path('admin/', admin.site.urls),
    path('', views.home),
    path('address/', include('address.urls')),
]