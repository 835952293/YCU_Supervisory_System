import hashlib
import json
import time

import jwt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from django.shortcuts import render
from django.views import View

# Create your views here.
from YCU_Supervisory_System.model.model import User


class Login(View):
    def post(self, resquest):
        data_json = resquest.body
        data = json.loads(data_json)
        account_id = data['account_id']
        pwd = data['password']
        try:
            user = User.objects.get(name=account_id)
            if user:
                # 密码验证
                m = hashlib.md5()
                m.update(pwd.encode())
                pwd_md5 = m.hexdigest()
                if user.password != pwd_md5:
                    return JsonResponse({'code': 10200, 'error': '密码错误'})
                # 密码正确，签发token
                token = self.make_token(account_id)
                return JsonResponse({
                    'code': 200,
                    'account_id': account_id,
                    'data': {'token': token},
                    'carts_count': 0
                })
        except Exception as e:
            print(e)
        return JsonResponse({'code': 10101, 'error': '用户名不存在'})

    @staticmethod
    def make_token(account_id, exp=24 * 60 * 60):
        payload = {
            'account_id': account_id,
            'exp': int(time.time()) + exp,
        }
        key = settings.JWT_TOKEN_KEY
        return jwt.encode(payload, key, algorithm='HS256').decode()


class Register(View):
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)

        account_id = json_obj["account_id"]
        password = json_obj["password"]
        phone = json_obj["phone"]
        email = json_obj["email"]
        try:
            user = User.objects.get(name=account_id)
            if user:
                return JsonResponse({'code': 10100, 'error': 'uname is exist'})
        except Exception as e:
            print(e)
            # 密码加密
            m = hashlib.md5()
            m.update(password.encode())
            password_md5 = m.hexdigest()

            try:
                User.objects.create(name=account_id, password=password_md5, email=email, phone=phone)
            except Exception as e:
                print('user create error %s' % e)
                result = {'code': 10101, 'error': 'uname is exist12321'}
                return JsonResponse(result)

            token = Login().make_token(account_id)
            result = {
                'code': 200,
                'username': account_id,
                'data': {'token': token},
                'cart_count': 0
            }
            return JsonResponse(result)


