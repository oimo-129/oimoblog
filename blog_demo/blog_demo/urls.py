"""
URL configuration for blog_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
#添加include模块
from django.urls import include
#添加测试日志
import logging

#获取日志记录器
logger = logging.getLogger('blog')

#使用日志
def log_view(request):
    try:
        # 记录日志
        logger.info('用户访问了首页')
        logger.debug('调试信息')
        
        # 返回响应
        return HttpResponse("Hello, 这是首页!")
    except Exception as e:
        logger.error(f'发生错误: {str(e)}')
        return HttpResponse("发生错误!", status=500)
        
        
        

urlpatterns = [
    path('admin/', admin.site.urls),   
    # 引入users应用的路由
    path('', include(('users.urls','users'),namespace='users')),
    #验证码
    path('captcha/', include('captcha.urls')),
    
]
