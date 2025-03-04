from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#验证码功能模块
from django.http import HttpResponseBadRequest,HttpResponse
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from django.views import View

# 注册
def resign(request):
    return render(request, 'register.html')



'''
验证码的生成：客户端发送请求，服务器端生成验证码和正确答案，将验证码和正确答案存储到redis中，返回验证码图片给客户端
验证码的校验：客户端发送请求，服务器端获取客户端传递的验证码和正确答案，校验验证码是否正确
'''

#图片库资源
class ImageCodeView(View):

    def get(self,request):
        #获取前端传递过来的参数
        uuid=request.GET.get('uuid')
        #判断参数是否为None
        if uuid is None:
            return HttpResponseBadRequest('请求参数错误')
        # 获取验证码内容和验证码图片二进制数据
        text, image = captcha.generate_captcha()
        # 将图片验内容保存到redis中，并设置过期时间
        redis_conn = get_redis_connection('default')
        redis_conn.setex('img:%s' % uuid, 300, text)
        # 返回响应，将生成的图片以content_type为image/jpeg的形式返回给请求
        return HttpResponse(image, content_type='image/jpeg')





#redis缓存
#template载入
#Vue调用