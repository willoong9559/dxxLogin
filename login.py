# -*- coding: utf-8 -*-
import re
import requests


class jqfyLogin(object):

    def __init__(self, class_all_id, class_id, username):
        # 初始化信息
        self.cookies = dict(laravel_session='eyJpdiI6IlwvQkhNQVBVWW5ocWV4RG43dVR0Uk9nPT0iLCJ2YWx1ZSI6Im9naU1hbmJqMTFveGtHT0xHOXdWbGVJWkpqa3ZqUmx0SWQySW1ZMGkrY29lY2U1UFhHOGp6dnpcL0V1bUttYjBKIiwibWFjIjoiZjE3MTQyOTllMWJjODZhZGFjYmMzZDIwOWIzZWQyZjM3NjYwYzExOWJhMWFjZjY5ZTIwOTFiNzM5MTFiNjE3ZSJ9')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'http://jqfy.jl54.org/study/select.html?pid=23',
            'Host': 'jqfy.jl54.org',
            'AUTHORIZATION': '0265b10041521df050bd8ce3726a3643',
            'Origin': 'http://jqfy.jl54.org',
            'Content - Type': 'application/x-www-form-urlencoded'
        }

        self.session = requests.Session()
        self.login_url = 'http://jqfy.jl54.org/home/add/study' #吉林省青年大学习，服务器日常抽风。
        self.post_url = 'http://jqfy.jl54.org/home/add/study'
        self.class_all_id = class_all_id
        self.class_id = class_id
        self.username = username

    def login_jqfy(self):
        # 登录入口
        post_data = {
            'class_all_id': self.class_all_id,
            'class_id': self.class_id,
            'username': self.username
        }
        r = requests.post(url=self.login_url, data=post_data, headers=self.headers)
        print(r.json())
        #print('StatusCode:', r.status_code)
        #if r.status_code != 200:
        #    print('Login Fail')

if __name__ == '__main__':
    class_all_id = ''
    class_id = ''
    username = ''
    # 抓包就有的

    login = jqfyLogin(class_all_id, class_id, username)
    login.login_jqfy()
