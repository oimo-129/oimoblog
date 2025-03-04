from django.urls import path
from . import views

app_name= 'users'

urlpatterns = [
    path('', views.resign, name='register'),
    #添加子路由
    path('image_code/',views.ImageCodeView.as_view(),name='image_code'),
]
