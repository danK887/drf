"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from strangecars.views import *
# используем роутеры для автоматизации запросов
router = routers.SimpleRouter()
router.register(r'cars', CarsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), #тут подключаем все урлы (доступ будет по ссылке http://127.0.0.1:8000/api/v1/cars/)
    path('api/v1/drf-auth/', include('rest_framework.urls')) #авторизация пользователя
    # прежние урлы для запросов get,post,put,delete,path
    # path('api/v1/carslist/', CarsAPIList.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarsAPIUpdate.as_view()),
    # path('api/v1/carslistdetail/<int:pk>/', CarsAPIDetail.as_view()),
]
