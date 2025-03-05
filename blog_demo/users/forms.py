from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    # 你的其他表单字段
    captcha = CaptchaField()
