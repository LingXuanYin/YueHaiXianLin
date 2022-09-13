# 用于获取edge或chrome中的cookie
# 调用getLocalCookie()返回一个字典

import base64
import json
import os
import sqlite3

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from win32crypt import CryptUnprotectData


class LocalCookie():
    # 获取encrypted_key
    def get_string(self, s_local_state):
        with open(s_local_state, 'r', encoding='utf-8') as f:
            s_encrtpted_key = json.load(f)['os_crypt']['encrypted_key']
        return s_encrtpted_key

    def pull_the_key(self, base64_encrypted_key):
        c_encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
        c_encrypted_key = c_encrypted_key_with_header[5:]
        c_key = CryptUnprotectData(c_encrypted_key, None, None, None, 0)[1]
        return c_key

    # v10版本解密
    def decrypt_string(self, c_key, c_data):
        c_nonce, c_cipherbytes = c_data[3:15], c_data[15:]
        aesgcm = AESGCM(c_key)
        c_plainbytes = aesgcm.decrypt(c_nonce, c_cipherbytes, None)
        s_plaintext = c_plainbytes.decode('utf-8')
        return s_plaintext

    # 获取 Chrome 或 Edge 登录本地cookies
    def get_cookie_from_chrome(self, s_browser_name='Chrome', s_host='.mihoyo.com'):
        """
            s_browser_name: 浏览器名称(Google Chrome, Microsoft Edge)
            s_host: 域名   例如： '.umeng.com'
        """
        # 获取相关浏览器本地cookie路径
        if s_browser_name == 'Chrome':
            s_path = r'\Google\Chrome\User Data\Local State'
            s_cookie = r'\Google\Chrome\User Data\Default\Network\Cookies'
        else:
            s_path = r'\Microsoft\Edge\User Data\Local State'
            s_cookie = r'\Microsoft\Edge\User Data\Default\Network\Cookies'
        # print('pass浏览器cookies本地路径：pass'.format(s_browser_name, s_cookie))
        s_local_state = os.environ['LOCALAPPDATA'] + s_path
        s_cookie_path = os.environ['LOCALAPPDATA'] + s_cookie
        sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % s_host
        # 获取d_cookie
        with sqlite3.connect(s_cookie_path) as conn:
            p_cursor = conn.cursor()
            p_res = p_cursor.execute(sql).fetchall()
            p_cursor.close()
            key = self.pull_the_key(self.get_string(s_local_state))
            d_cookie = dict()
            for s_host_key, s_name, c_encrypted_value in p_res:
                if c_encrypted_value[0:3] == b'v10':
                    d_cookie[s_name] = self.decrypt_string(key, c_encrypted_value)
                else:
                    d_cookie[s_name] = CryptUnprotectData(c_encrypted_value)[1].decode()

            return d_cookie

    @staticmethod
    def dict_to_str(d_cookie: dict):
        _s = ''
        for _k in list(d_cookie.keys()):
            _s += f'{_k}={d_cookie[_k]};'
        return _s
