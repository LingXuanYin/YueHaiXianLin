# @https://github.com/Le-niao/Yunzai-Bot/blob/master/lib/app/mysApi.js
# python实现by:南辰燏炚@https://github.com/LingXuanYin/YueHaiXianLin/blob/master/mysapi.py
import hashlib
import json
import os
import random
import time

import requests

import LocalCookie

APP_VERSION = "2.33.1"
APP_VERSION_SIGN = "2.34.1"

SALT_2_33_1 = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
SALT_2_34_1 = "9nQiU3AV0rJSIBWgdynfoGMGKaklfbM7"

HOST = "https://api-takumi.mihoyo.com"
HOST_record = "https://api-takumi-record.mihoyo.com"
GAME_record = "/game_record/app/genshin/api/"

PATH_self = os.path.join(os.getcwd(), 'MYS')
PATH_userdata = os.path.join(os.getcwd(), 'UserData')


class Cookie(LocalCookie.LocalCookie):

    def __init__(self, cookies=None):
        self.cookies = cookies
        pass

    @staticmethod
    def fatchCookie(sCookie):
        _sC = sCookie
        jCookie = {}
        try:
            jCookie['_gat'] = _sC[_sC.index('_gat=') + 5: _sC.index('_gat=') + 5 + 1]
        except:
            pass
        try:
            jCookie['_ga'] = _sC[_sC.index('_ga=') + 4: _sC.index('_ga=') + 4 + 27]
        except:
            pass
        try:

            jCookie['_gid'] = _sC[_sC.index('_gid=') + 5: _sC.index('_gid=') + 5 + 27]
        except:
            pass
        try:
            jCookie['_MHYUUID'] = _sC[_sC.index('_MHYUUID=') + 9: _sC.index('_MHYUUID=') + 9 + 36]
        except:
            pass
        try:
            jCookie['ltoken_v2'] = _sC[_sC.index('ltoken_v2=') + 7: _sC.index('ltoken_v2=') + 7 + 40]
        except:
            raise Exception('Cookie 不完整，缺失 ltoken')
        try:
            jCookie['ltuid_v2'] = _sC[_sC.index('ltuid_v2=') + 6: _sC.index('ltuid_v2=') + 6 + 9]
        except:
            raise Exception('Cookie 不完整，缺失 ltuid')
        try:
            jCookie['cookie_token_v2'] = _sC[_sC.index('cookie_token_v2=') + 13: _sC.index('cookie_token_v2=') + 13 + 40]
        except:
            pass
            # raise Exception('Cookie 不完整，缺失 cookie_token')
        try:
            jCookie['account_id_v2'] = jCookie['ltuid_v2']
        except:
            pass
        try:
            jCookie['account_mid_v2'] = jCookie['ltuid_v2']
        except:
            pass


        # print(jCookie)
        return jCookie

    @staticmethod
    def checkCookie(_cookie):
        API = mys(_cookie)
        API.checkResponse(API.getUserGameRoles())
        # API.checkResponse(API.getDailyNote())
        return True


class mys():
    def __init__(self, cookie: dict):
        self.COOKIES = cookie
        self.TOKEN = self.getToken()
        # print(self.TOKEN)
        self.UID_GAME = ''
        self.UID_MYS = self.getUID_MYS()
        self.PROXY = None

    def getToken(self):
        if 'cookie_token_v2' in self.COOKIES.keys() and 'ltuid_v2' in self.COOKIES.keys() and 'ltoken_v2' in self.COOKIES.keys():
            return 'ltoken_v2=' + self.COOKIES['ltoken_v2'] + ';ltuid_v2=' + self.COOKIES["ltuid_v2"] + ';' + 'cookie_token_v2=' + \
                   self.COOKIES["cookie_token_v2"] + ';' + 'account_id_v2=' + self.COOKIES["ltuid_v2"] + ';' + 'account_mid_v2=' + \
                   self.COOKIES['account_mid_v2'] + ';' + 'ltmid_v2=' + self.COOKIES['ltmid_v2']+';'
        elif 'ltuid_v2' in self.COOKIES.keys() and 'ltoken_v2' in self.COOKIES.keys():
            return 'ltoken_v2=' + self.COOKIES['ltoken_v2'] + ';ltuid_v2=' + self.COOKIES["ltuid_v2"] + ';' + 'account_id_v2=' + \
                   self.COOKIES["ltuid_v2"] + ';' + 'account_mid_v2=' + \
                   self.COOKIES['account_mid_v2'] + ';' + 'ltmid_v2=' + self.COOKIES['ltmid_v2']+';'
        else:
            raise Exception('Cookie keys ERROR')

    def getUID_MYS(self):
        return self.COOKIES['ltuid_v2']

    def checkResponse(self, response):
        # print(response.json())
        # print(self.TOKEN)
        if response.status_code != 200:
            raise Exception('API ERROR')
        response = response.json()
        if response['retcode'] != -5003 and response['retcode'] != 0:
            if response['retcode'] == -100:
                raise Exception(response['message'])
            raise Exception(response['message'])

        return response

    def getServer(self, uid):
        # print(uid)
        # print(self.COOKIES)
        if str(uid)[0] == '1' or str(uid)[0] == '2':
            return "cn_gf01"  # 官服
        elif str(uid)[0] == '5':
            return "cn_qd01"  # B服
        else:
            raise Exception('UID ERROR in mys.getServer()')

    def getDs(self, q="", b=""):  # DS算法
        n = SALT_2_33_1
        r = str(random.randint(100000, 900000))
        t = str(int(time.time() + 8 * 60 * 60 / 1000) + 1)  # UTF+8
        md5_str = 'salt=' + n + '&t=' + t + '&r=' + r + '&b=' + b + '&q=' + q
        DS = hashlib.md5(md5_str.encode('UTF-8')).hexdigest()
        return t + ',' + r + ',' + DS

    def getDS_sign(self):  # 签到DS算法
        n = SALT_2_34_1
        t = str(int(time.time() + 8 * 60 * 60 / 1000) + 1)  # UTF+8
        r = ''
        buf = 'abcdefghijklmnopqrstuvwxyz0123456789'
        i = 0
        while i < 6:
            c = buf[random.randint(0, len(buf) - 1)]
            if c not in r:
                r += c
                i += 1
        md5_str = 'salt=' + n + '&t=' + t + '&r=' + r
        DS = hashlib.md5(md5_str.encode('UTF-8')).hexdigest()
        return t + ',' + r + ',' + DS

    def guid(self):
        def S4():
            return hex(int((random.random() + 1) * 0x10000))[3:]  # [3:0] 去掉0x及其后面一位

        return S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4()

    def getUrl(self, type, uid, data={}):

        host = HOST
        host_record = HOST_record
        game_record = GAME_record

        query, body, url = '', '', ''

        server = self.getServer(uid)

        # 首页宝箱
        if type == "index":
            url = host_record + game_record + "index"
            query = 'role_id=' + uid + '&server=' + server

        # 深渊
        elif type == "spiralAbyss":
            url = host_record + game_record + "spiralAbyss"
            query = 'role_id=' + uid + '&schedule_type=' + data['schedule_type'] + '&server=' + server

        # 角色详情
        elif type == "character":
            url = host_record + game_record + "character"
            body = json.dumps(data)

        # 树脂每日任务（只能当前id）
        elif type == "dailyNote":
            url = host_record + game_record + "dailyNote"
            query = 'role_id=' + uid + '&server=' + server

        elif type == "detail":
            url += host + "/event/e20200928calculate/v1/sync/avatar/detail"
            query = 'uid=' + uid + '&region=' + server + '&avatar_id=' + data['avatar_id']

        elif type == "getAnnouncement":
            url += host_record + "/game_record/card/wapi/getAnnouncement"

        elif type == "getGameRecordCard":
            url += host_record + "/game_record/card/wapi/getGameRecordCard"
            query = 'uid=' + uid  # 米游社id

        elif type == "bbs_sign_info":
            url += host + "/event/bbs_sign_reward/info"
            query = 'act_id=e202009291139501&region=' + server + '&uid=' + uid

        elif type == "bbs_sign_home":
            url += host + "/event/bbs_sign_reward/home"
            query = 'act_id=e202009291139501&region=' + server + '&uid=' + uid

        elif type == "bbs_sign":
            url += host + "/event/bbs_sign_reward/sign"
            body = json.dumps({'act_id': "e202009291139501", 'region': server, 'uid': uid, })

        elif type == "ys_ledger":
            url = "https://hk4e-api.mihoyo.com/event/ys_ledger/monthInfo"
            query = 'month=' + data['month'] + '&bind_uid=' + uid + '&bind_region=' + server

        if query:
            url += "?" + query

        if type == "bbs_sign":
            headers = self.getHeaders_sign()
        else:
            headers = self.getHeaders(query, body)
        return url, headers, query, body

    def getHeaders(self, q="", b=""):
        headers = {
            "x-rpc-app_version": APP_VERSION,
            "x-rpc-client_type": '5',
            'DS': self.getDs(q, b),
        }

        return headers

    def getHeaders_sign(self):
        global GS_uid
        headers = {
            "x-rpc-app_version": APP_VERSION_SIGN,
            "x-rpc-client_type": '5',
            "x-rpc-device_id": self.guid(),
            # "User-Agent": "miHoYoBBS/2.3.0",
            # 'Content-Type': 'application/json',
            "DS": self.getDS_sign()
        }
        return headers

    def getUserGameRoles(self):

        headers = self.getHeaders()
        headers['Cookie'] = self.TOKEN
        _url = "https://api-takumi.mihoyo.com/" + "binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn"

        response = requests.get(url=_url, headers=headers, proxies=self.PROXY)
        print(response.text)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())

        self.DATA_ROAL = response.json()['data']
        self.UID_GAME = self.DATA_ROAL['list'][0]['game_uid']
        self.UID_MYS = self.COOKIES['ltuid_v2']
        return response

    def getDailyNote(self):
        if self.UID_GAME == '':
            self.getUserGameRoles()
        url, headers, query, body = self.getUrl("dailyNote", self.UID_GAME)
        headers['Cookie'] = self.TOKEN

        response = requests.get(url=url, headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())

        self.DATA_DAILYNOTE = response.json()['data']
        return response

    # 便签开关
    def openDailyNote(self):
        if self.UID_GAME == '':
            self.getUserGameRoles()

        url = HOST_record + "/game_record/card/wapi/getGameRecordCard?uid="
        change_url = HOST_record + "/game_record/card/wapi/changeDataSwitch"
        query = ""
        body = {"is_public": 'true', "switch_id": '3', "game_id": "2"}
        headers = self.getHeaders(query, json.dumps(body))
        headers['Cookie'] = self.TOKEN
        account_id = self.UID_MYS
        url = url + account_id
        response = requests.get(url=url, headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())
        response = requests.post(url=change_url, data=json.dumps(body), headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())

        return response

    def bbs_sign(self):
        if self.UID_GAME == '':
            self.getUserGameRoles()

        url, headers, query, body = self.getUrl('bbs_sign', self.UID_GAME)
        headers['Cookie'] = self.TOKEN

        response = requests.post(url=url, data=body, headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())
        return response

    def bbs_sign_info(self):
        if self.UID_GAME == '':
            self.getUserGameRoles()

        url, headers, query, body = self.getUrl("bbs_sign_info", self.UID_GAME)
        headers['Cookie'] = self.TOKEN

        response = requests.get(url, headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())
        return response

    def bbs_sign_home(self):
        if self.UID_GAME == '':
            self.getUserGameRoles()

        url, headers, query, body = self.getUrl("bbs_sign_home", self.UID_GAME)
        headers['Cookie'] = self.TOKEN

        response = requests.get(url=url, headers=headers, proxies=self.PROXY)
        if not self.checkResponse(response): raise Exception('Unexpected response: ' + response.json())
        return response

    def get_awards_today(self):
        _awards = self.bbs_sign_home().json()['data']['awards']
        _sign_info = self.bbs_sign_info().json()['data']
        _today = _sign_info['total_sign_day']  # +_sign_info['sign_cnt_missed']
        return _awards[_today - 1]  # 返回当天奖励的dict
