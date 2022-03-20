"""
    登入状态校验装饰器
"""
import jwt
from django.http import JsonResponse

from django.conf import settings

from model.models import User


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({'code': 403, 'error': 'Pleace login'})
        try:
            payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
        except Exception as e:
            print(e)
            return JsonResponse({'code': 403, 'error': 'Pleace login'})
        username = payload['username']
        user = User.objects.get(name=username)
        request.user = user
        return func(self, request, *args, **kwargs)
    return wrapper
