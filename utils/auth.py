#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import hashlib
from AutoCmdb.settings import ASSET_AUTH_HEADER_NAME
from AutoCmdb.settings import ASSET_AUTH_KEY
from AutoCmdb.settings import ASSET_AUTH_TIME
from django.http import JsonResponse

ENCRYPT_LIST = [
    # {'encrypt': encrypt, 'time': timestamp
]


def api_auth_method(request):
    auth_key = request.META.get('HTTP_AUTH_KEY')
    if not auth_key:
        return False
    sp = auth_key.split('|')
    if len(sp) != 2:
        return False
    encrypt, timestamp = sp
    timestamp = float(timestamp)
    limit_timestamp = time.time() - ASSET_AUTH_TIME
    # 是否超时
    if limit_timestamp > timestamp:
        return False
    ha = hashlib.md5(ASSET_AUTH_KEY.encode('utf-8'))
    ha.update(bytes("%s|%f" % (ASSET_AUTH_KEY, timestamp), encoding='utf-8'))
    result = ha.hexdigest()
    # 加密对比验证
    if encrypt != result:
        return False

    exist = False
    del_keys = []
    for k, v in enumerate(ENCRYPT_LIST):
        print(k, v)
        m = v['time']
        n = v['encrypt']
        if m < limit_timestamp:
            del_keys.append(k)
            continue
        if n == encrypt:
            exist = True
    for k in del_keys:
        del ENCRYPT_LIST[k]
    # 判断列表中是否已存在
    if exist:
        return False
    ENCRYPT_LIST.append({'encrypt': encrypt, 'time': timestamp})
    return True


def api_auth(func):
    def inner(request, *args, **kwargs):
        if not api_auth_method(request):
            return JsonResponse({'code': 1001, 'message': 'API授权失败'}, json_dumps_params={'ensure_ascii': False})
        return func(request, *args, **kwargs)

    return inner