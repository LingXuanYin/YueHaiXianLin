import copy
import json
import os
import threading
import time
from urllib.parse import unquote

import pyecharts
import requests
import win32api
import win32con
from win32clipboard import GetClipboardData, OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData

PATH_SELF = os.getcwd()
PATH_USERDATA = os.path.join(PATH_SELF, 'DATA')
PATH_CACHEDATA = os.path.join(PATH_SELF, 'cache')

# URL_OS = '''https://hk4e-api-os.hoyoverse.com/event/gacha_info/api/getGachaLog'''
# URL_CN = '''https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'''


class Tool():  # 工具类函数

    @staticmethod
    def gachaType_transFromcode(code):
        # print(code)
        if code == 200 or code == '200':
            return '常驻祈愿'
        elif code == 302 or code == '302':
            return '武器活动祈愿'
        elif code == 400 or code == '400' or code == 301 or code == '301':
            return '角色活动祈愿'
        elif code == 100 or code == '100':
            return '新手祈愿'
        else:
            raise ValueError('Unexpected gacha type')

    @staticmethod
    def gachaType_transFromcode_En(code):
        # print(code)
        if code == 200 or code == '200':
            return 'permanent'
        elif code == 302 or code == '302':
            return 'wap'
        elif code == 400 or code == '400' or code == 301 or code == '301':
            return 'char'
        elif code == 100 or code == '100':
            return 'novice'
        else:
            raise ValueError('Unexpected gacha type')

    @staticmethod
    # 读取剪贴板的数据
    def get_clipboard():
        OpenClipboard()
        d = GetClipboardData(win32con.CF_TEXT)
        CloseClipboard()
        return d.decode('UTF-8')

    @staticmethod
    # 写入剪贴板数据
    def set_clipboard(astr):
        OpenClipboard()
        EmptyClipboard()
        # time.sleep(1)
        SetClipboardData(win32con.CF_UNICODETEXT, astr)
        CloseClipboard()

    @staticmethod
    def dict_to_list(dict: dict):  # 字典转列表
        dictlist = []
        for keys, value in dict.items():
            temp = [keys, value]
            dictlist.append(temp)
        # print(dictlist)
        return dictlist

    @staticmethod
    def get(src_url, src_data, PROXY=None):  # get数据
        src_data['timestamp'] = int(time.time())  # 使用实时时间
        if PROXY:
            response = requests.get(src_url, src_data, proxies=PROXY, timeout=10)  # 超时10s，使用代理
        else:
            response = requests.get(src_url, src_data)
        # print(response.text)
        if response.json()['message'] == 'OK' and response.json()['retcode'] == 0:
            return eval(response.text)['data']['list']
        elif 'visit too frequently' in response.text:
            time.sleep(0.5)  # 防止请求频繁
            return 'visit too frequently'
        else:
            raise ValueError("URL ERROR")


class UserData():
    def __init__(self, user_id):
        self.USER_ID = user_id
        self.DBM_UD = DatabaseManager('UserData')
        self.DBM_URL = DatabaseManager('URL')
        if user_id not in list(self.DBM_UD.DATA.keys()):
            self.DBM_UD.set_NodeData(user_id, {"char": [], "wap": [], "permanent": [], "novice": []})
        if self.DBM_UD.get_NodeData(user_id) == {}:
            self.DBM_UD.set_NodeData(user_id, {"char": [], "wap": [], "permanent": [], "novice": []})
        if user_id not in list(self.DBM_URL.DATA.keys()):
            self.DBM_URL.set_NodeData(user_id, '')

        self.USER_GACHADATA = self.DBM_UD.get_NodeData(user_id)
        # print(self.USER_GACHADATA)
        self.novice = self.USER_GACHADATA['novice']
        self.permanent = self.USER_GACHADATA['permanent']
        self.wap = self.USER_GACHADATA['wap']
        self.char = self.USER_GACHADATA['char']


class DatabaseManager():
    def __init__(self, DB_NAME):
        self.DB_NAME = DB_NAME
        try:
            self.DATA = json.load(open(f'./DATA/{DB_NAME}.json', 'r', encoding='UTF-8'))
        except:
            raise RuntimeError(f"读取数据库错误：{DB_NAME}.json")

    def get_NodeData(self, node):
        return self.DATA[node]

    def set_NodeData(self, node, data):
        self.DATA[node] = data
        json.dump(self.DATA, open(f'./DATA/{self.DB_NAME}.json', 'w+', encoding='UTF-8'))


class _URL():
    HOST_CN = r'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'
    HOST_OS = r'https://hk4e-api-os.hoyoverse.com/event/gacha_info/api/getGachaLog'

    def __init__(self):
        # 节点名为user_id
        self.DBM = DatabaseManager('URL')

    @staticmethod
    def getServer(URL):
        if _URL.HOST_CN in URL:
            return 'CN'
        elif _URL.HOST_OS in URL:
            return 'OS'
        else:
            raise ValueError('Unexpected Server')

    def scanURL(self, game_path: str):
        if not os.path.exists(os.path.join(game_path, r'YuanShen_Data\webCaches\Cache\Cache_Data')):
            raise ValueError('游戏目录错误')
        _P = os.path.join(game_path, r'YuanShen_Data\webCaches\Cache\Cache_Data')

        _f = os.path.join(_P, 'data_2')
        _fdata = []
        _url = None
        _buf = {}
        win32api.CopyFile(_f, 'cache/URL_cache')
        _fdata = open('cache/URL_cache', 'rb').readlines()
        os.remove('cache/URL_cache')

        for _l in _fdata:
            if self.HOST_CN.encode(encoding='UTF-8') in _l:
                _start = _l.rfind(self.HOST_CN.encode(encoding='UTF-8'))
                _end = _l.rfind('&game_biz=hk4e_cn'.encode(encoding='UTF-8')) + len('&game_biz=hk4e_cn')
                _url = _l[_start:_end].decode(encoding='UTF-8')
                _uid = self.checkURL(_url)
                if _uid != 0:
                    _buf[_uid] = _url
                else:
                    pass

        return _buf
        # break

    @staticmethod
    def transURL( url_forfirst, gacha_type, page, end_id):
        #print(url_forfirst)
        authkey_ver = int(url_forfirst[url_forfirst.rfind('authkey_ver=') + 12])
        sign_type = int(url_forfirst[url_forfirst.rfind('sign_type=') + 10])
        auth_appid = url_forfirst[url_forfirst.rfind('auth_appid=') + 11:url_forfirst.rfind('&init_type')]
        init_type = int(url_forfirst[url_forfirst.rfind('init_type=') + 10:url_forfirst.rfind('&gacha_id')])
        gacha_id = url_forfirst[url_forfirst.rfind('gacha_id=') + 9:url_forfirst.rfind('&timestamp')]
        timestamp = int(url_forfirst[url_forfirst.rfind('timestamp=') + 10:url_forfirst.rfind('&lang')])
        device_type = url_forfirst[url_forfirst.rfind('device_type=') + 12:url_forfirst.rfind('&game_version')]
        game_version = url_forfirst[url_forfirst.rfind('game_version=') + 13:url_forfirst.rfind('&plat_type')]
        plat_type = url_forfirst[url_forfirst.rfind('plat_type=') + 10:url_forfirst.rfind('&region')]
        region = url_forfirst[url_forfirst.rfind('region=') + 7:url_forfirst.rfind('&authkey')]
        authkey = url_forfirst[url_forfirst.rfind('authkey=') + 8:url_forfirst.rfind('&game_biz')]
        game_biz = url_forfirst[url_forfirst.rfind('game_biz=') + 9:]
        data = {
            'authkey_ver': authkey_ver,
            'sign_type': sign_type,
            'auth_appid': auth_appid,
            'init_type': init_type,
            'gacha_id': gacha_id,
            'timestamp': timestamp,
            'lang': 'zh-cn',
            'device_type': device_type,
            'game_version': game_version,
            'plat_type': plat_type,
            'region': region,
            'authkey': unquote(authkey),  #
            'game_biz': game_biz,
            'gacha_type': gacha_type,
            'page': page,
            'size': 20,
            'end_id': end_id
        }
        if 'cn' not in region:
            return _URL.HOST_OS, data
        else:
            return _URL.HOST_CN, data

    def getURL(self, user_id):
        if self.checkURL(self.DBM.get_NodeData(user_id)):
            return self.DBM.get_NodeData(user_id)
        else:
            raise TimeoutError('链接已失效')

    def updateURL(self):
        user_id, _url = self.scanURL(DatabaseManager('GamePath').get_NodeData('path'))
        self.DBM.set_NodeData(user_id, _url)

    @staticmethod
    def checkURL( url):
        try:
            _url, _data = _URL.transURL(url, 301, 1, 0)
            UID = Tool.get(_url, _data)[0]['uid']  # 获取一次以校验链接
            #print(_url)
            return UID
        except Exception as e:
            # raise e
            # print(e)
            return 0


class GachaData():

    def __init__(self, UDBM: UserData):

        self.UDBM = UDBM
        self.URL, self.AUTHDATA = _URL().transURL(self.UDBM.DBM_URL.get_NodeData(UDBM.USER_ID), 301, 1, 0)
        self.THREAD_FLAG=0

    def SrcData_processor(self, response_list, gacha_type):

        def _process_response(response_list: list, data_list: list):
            for _i in response_list:
                if _i not in data_list:
                    # if _i['item_id'] !='':
                    #     print(_i)
                    data_list.append(_i)

        if response_list == []:
            return  # 跳过空列表
        if gacha_type == 400 or gacha_type == 301:  # 角色活动祈愿
            _process_response(response_list, self.UDBM.char)
        elif gacha_type == 302:  # 武器活动祈愿
            _process_response(response_list, self.UDBM.wap)
        elif gacha_type == 200:  # 常驻祈愿
            _process_response(response_list, self.UDBM.permanent)
        elif gacha_type == 100:  # 新手祈愿
            _process_response(response_list, self.UDBM.novice)
        else:
            raise Exception(f'Unexpected gacha_type{gacha_type}')

    # 导入数据
    def UserData_import(self, _userdata: list):
        for _i in _userdata:

            if _i['gacha_type'] == 400 or _i['gacha_type'] == 301 or _i['gacha_type'] == '400' or _i['gacha_type'] == '301':  # 角色活动祈愿
                if _i not in self.UDBM.char:
                    self.UDBM.char.append(_i)
            elif _i['gacha_type'] == 302 or _i['gacha_type'] == '302':  # 武器活动祈愿
                if _i not in self.UDBM.wap:
                    self.UDBM.wap.append(_i)
            elif _i['gacha_type'] == 200 or _i['gacha_type'] == '200':  # 常驻祈愿
                if _i not in self.UDBM.permanent:
                    self.UDBM.permanent.append(_i)
            elif _i['gacha_type'] == 100 or _i['gacha_type'] == '100':  # 新手祈愿
                if _i not in self.UDBM.novice:
                    self.UDBM.novice.append(_i)
            else:
                raise Exception(f'Unexpected gacha_type{_i["gacha_type"]}')
        # 重排序
        self.UDBM.char = sorted(self.UDBM.char, key=lambda x: x['id'], reverse=True)
        self.UDBM.wap = sorted(self.UDBM.wap, key=lambda x: x['id'], reverse=True)
        self.UDBM.permanent = sorted(self.UDBM.permanent, key=lambda x: x['id'], reverse=True)
        self.UDBM.novice = sorted(self.UDBM.novice, key=lambda x: x['id'], reverse=True)
        # 保存
        self.UDBM.DBM_UD.set_NodeData(self.UDBM.USER_ID,
                                      {'char': self.UDBM.char, 'wap': self.UDBM.wap, 'permanent': self.UDBM.permanent,
                                       'novice': self.UDBM.novice})

    def GetSrcdata(self, _url, _data: dict, gacha_type):
        self.THREAD_FLAG=self.THREAD_FLAG+1
        _data['page'] = 1
        _data['end_id'] = 0
        _data['gacha_type'] = gacha_type
        while True:

            response_list = Tool().get(_url, _data)
            if response_list == []: break  # 无数据提前跳出
            if response_list == 'visit too frequently':
                continue  # 防止请求频繁
            else:
                for sth in response_list:
                    sth['id'] = int(sth['id'])
                self.SrcData_processor(response_list, gacha_type)  # 送至处理函数
            if len(response_list) != 20: break  # 最后一页跳出
            # 处理结束ID
            _data['end_id'] = response_list[len(response_list) - 1]['id']
            # 处理页数
            _data['page'] += 1
        self.THREAD_FLAG=self.THREAD_FLAG-1

    def Main_DataGetter(self):
        _url = self.URL
        _authdata = self.AUTHDATA
        _th301 = threading.Thread(target=self.GetSrcdata, args=((_url, copy.deepcopy(_authdata), 301,)))
        _th400 = threading.Thread(target=self.GetSrcdata, args=((_url, copy.deepcopy(_authdata), 400,)))
        _th302 = threading.Thread(target=self.GetSrcdata, args=((_url, copy.deepcopy(_authdata), 302,)))
        _th200 = threading.Thread(target=self.GetSrcdata, args=((_url, copy.deepcopy(_authdata), 200,)))
        #_th100 = threading.Thread(target=self.GetSrcdata, args=((_url, copy.deepcopy(_authdata), 100,)))
        # _th301.setDaemon(False)
        # _th400.setDaemon(False)
        # _th302.setDaemon(False)
        # _th200.setDaemon(False)
        _th301.start()
        _th400.start()
        _th302.start()
        _th200.start()
        #_th100.start()
        #print('start')
        # self.UDBM.DBM_UD.set_NodeData(self.UDBM.USER_ID,
        #                               {'char': self.UDBM.char, 'wap': self.UDBM.wap, 'permanent': self.UDBM.permanent,
        #                                'novice': self.UDBM.novice})

        #return self.UDBM


class echarts():  # 图表类
    def __init__(self, DataBase: UserData):
        self.UDBM = DataBase
        # 重排序
        self.UDBM.char = sorted(self.UDBM.char, key=lambda x: x['id'], reverse=True)
        self.UDBM.wap = sorted(self.UDBM.wap, key=lambda x: x['id'], reverse=True)
        self.UDBM.permanent = sorted(self.UDBM.permanent, key=lambda x: x['id'], reverse=True)
        self.UDBM.novice = sorted(self.UDBM.novice, key=lambda x: x['id'], reverse=True)

        self._char = copy.deepcopy(self.UDBM.char)
        self._wap = copy.deepcopy(self.UDBM.wap)
        self._permanent = copy.deepcopy(self.UDBM.permanent)
        self._novice = copy.deepcopy(self.UDBM.novice)

    def _pre_process(self, _data: list):
        _l3, _l4, _l5 = [], [], []
        for _item in _data:
            _item['index'] = _data.index(_item) + 1
            if _item['rank_type'] == '3':
                _l3.append(_item)
            elif _item['rank_type'] == '4':
                _l4.append(_item)
            elif _item['rank_type'] == '5':
                _l5.append(_item)
        _l3 = sorted(_l3, key=lambda x: x['id'], reverse=True)
        _l4 = sorted(_l4, key=lambda x: x['id'], reverse=True)
        _l5 = sorted(_l5, key=lambda x: x['id'], reverse=True)
        return {'3': _l3, '4': _l4, '5': _l5, 'gacha_type': _data[0]['gacha_type']}

    # 构造出货列表
    def _make_detail(self, _pre_data: dict):
        _detail3, _detail4, _detail5 = '', '', ''
        _l3 = {}
        for _i in _pre_data['3']:
            if _i['name'] not in list(_l3.keys()):
                _l3[_i['name']] = 0
            _l3[_i['name']] += 1

        _l3 = Tool.dict_to_list(_l3)
        _l3 = sorted(_l3, key=lambda x: x[1], reverse=True)

        for _i in _l3:
            _detail3 += f' [{_i[1]}]{_i[0]}'
        for _i in _pre_data['4']:
            if _pre_data['4'].index(_i) == len(_pre_data['4']) - 1:
                _detail4 += f' [N/A]{_i["name"]}'
            else:
                _detail4 += f' [{_pre_data["4"][_pre_data["4"].index(_i) + 1]["index"] - _i["index"]}]{_i["name"]}'
        for _i in _pre_data['5']:
            if _pre_data['5'].index(_i) == len(_pre_data['5']) - 1:
                _detail5 += f' [N/A]{_i["name"]}'
            else:
                _detail5 += f' [{_pre_data["5"][_pre_data["5"].index(_i) + 1]["index"] - _i["index"]}]{_i["name"]}'

        return _detail3, _detail4, _detail5

    def make_pie(self, _pre_data: dict):  # 构造饼图对象，传入数据类
        _detail3, _detail4, _detail5 = self._make_detail(_pre_data)
        _pie_percent = [['三星', len(_pre_data['3'])], ['四星', len(_pre_data['4'])], ['五星', len(_pre_data['5'])]]

        charts_name = Tool.gachaType_transFromcode(_pre_data['gacha_type'])

        total_count = len(_pre_data['3']) + len(_pre_data['4']) + len(_pre_data['5'])
        pie = (
            pyecharts.charts.Pie(init_opts=pyecharts.options.InitOpts(chart_id=charts_name, bg_color='#282C34'))  # 设置id
            .add(
                charts_name,
                _pie_percent,

                tooltip_opts=pyecharts.options.TooltipOpts  # 内容框设置
                    (

                    border_color='#66CCFF',
                    background_color='#282C34',
                    border_width=1,
                    trigger_on='mousemove|click',
                    # 内嵌JS回调函数使数据随鼠标指向的图表变动，展示具体记录
                    formatter=pyecharts.globals.JsCode('''function(parg){\n
                    if( parg.name == '三星')\n
                    {\n
                    return ' 三星： ''' + str(len(_pre_data['3'])) + ' ( ' + str(
                        int((len(_pre_data['3']) / total_count) * 10000) / 100) + ''' % )</br>' ;\n
                    }else if (parg.name == '四星')\n
                    {\n
                    return ' 四星： ''' + str(len(_pre_data['4'])) + ' ( ' + str(
                        int(((len(_pre_data['4'])) / total_count) * 10000) / 100) + ''' % )</br>';\n
                    }else if (parg.name == '五星')\n
                    {\n
                    return ' 五星： ''' + str(len(_pre_data['5'])) + ' ( ' + str(
                        int(((len(_pre_data['5'])) / total_count) * 10000) / 100) + ''' % )</br>';\n
                    }\n
                }\n'''),
                    textstyle_opts=pyecharts.options.TextStyleOpts(font_size=16, color='#66CCFF'),

                ),
                radius=["35%", "70%"],
            )
            .set_global_opts(title_opts=pyecharts.options.TitleOpts(charts_name,
                                                                    title_textstyle_opts=pyecharts.options.TextStyleOpts(
                                                                        color='#66CCFF')))
            # 设置标题
        ).add_js_funcs('''
option_defult = {
        series: [{
            type:'pie',
                name:''' + charts_name + ''',
                
                color:["skyblue","purple","yellow"],
                
                itemStyle: {
                    Radius: 5,
                    borderColor: 'yellow',
                    borderWidth: 2
                            },
                startAngle:-75,
                selectedMode: 'single',
                label: {
                    position: 'outside',
                    fontSize: 20,
                    }
            }]
        };
        chart_''' + charts_name + '''.setOption(option_defult);''')  # 以额外的js代码设置样式
        pie.width = '420px'
        pie.height = '410px'
        # 保存格式化之后的数据
        return pie

    def draw_charts(self):  # 绘制所有图表对象
        # _pie=[]
        if self._char != []:
            _pie = self.make_pie(self._pre_process(self._char))
            _page = pyecharts.charts.Page(page_title=f'山泽麟迹{self.UDBM.USER_ID}_c1')
            _page.add(_pie)
            _page.render('./cache/cache.html')
            _page.save_resize_html(source='./cache/cache.html', dest=f'./DATA/charts/{self.UDBM.USER_ID}_c1.html',
                                   cfg_dict=[{"cid": "角色活动祈愿", "width": "430px", "height": "410px", "top": "0px",
                                              "left": "0px"}])
            _b = open(f'./DATA/charts/{self.UDBM.USER_ID}_c1.html', 'r', encoding='UTF-8').read().replace(
                'https://assets.pyecharts.org/assets/echarts.min.js', 'echarts.js')
            open(f'./DATA/charts/{self.UDBM.USER_ID}_c1.html', 'w+', encoding='UTF-8').write(_b)

        if self._wap != []:
            _pie = self.make_pie(self._pre_process(self._wap))
            _page = pyecharts.charts.Page(page_title=f'山泽麟迹{self.UDBM.USER_ID}_c2')
            _page.add(_pie)
            _page.render('./cache/cache.html')
            _page.save_resize_html(source='./cache/cache.html', dest=f'./DATA/charts/{self.UDBM.USER_ID}_c2.html',
                                   cfg_dict=[{"cid": "武器活动祈愿", "width": "430px", "height": "410px", "top": "0px",
                                              "left": "0px"}])
            _b = open(f'./DATA/charts/{self.UDBM.USER_ID}_c2.html', 'r', encoding='UTF-8').read().replace(
                'https://assets.pyecharts.org/assets/echarts.min.js', 'echarts.js')
            open(f'./DATA/charts/{self.UDBM.USER_ID}_c2.html', 'w+', encoding='UTF-8').write(_b)

        if self._novice != []:
            _pie = self.make_pie(self._pre_process(self._novice))
            _page = pyecharts.charts.Page(page_title=f'山泽麟迹{self.UDBM.USER_ID}_c4')
            _page.add(_pie)
            _page.render('./cache/cache.html')
            _page.save_resize_html(source='./cache/cache.html', dest=f'./DATA/charts/{self.UDBM.USER_ID}_c4.html',
                                   cfg_dict=[{"cid": "新手祈愿", "width": "430px", "height": "410px", "top": "0px",
                                              "left": "0px"}])
            _b = open(f'./DATA/charts/{self.UDBM.USER_ID}_c4.html', 'r', encoding='UTF-8').read().replace(
                'https://assets.pyecharts.org/assets/echarts.min.js', 'echarts.js')
            open(f'./DATA/charts/{self.UDBM.USER_ID}_c4.html', 'w+', encoding='UTF-8').write(_b)
        if self._permanent != []:
            _pie = self.make_pie(self._pre_process(self._permanent))
            _page = pyecharts.charts.Page(page_title=f'山泽麟迹{self.UDBM.USER_ID}_c3')
            _page.add(_pie)
            _page.render('./cache/cache.html')
            _page.save_resize_html(source='./cache/cache.html', dest=f'./DATA/charts/{self.UDBM.USER_ID}_c3.html',
                                   cfg_dict=[{"cid": "常驻祈愿", "width": "430px", "height": "410px", "top": "0px",
                                              "left": "0px"}])
            _b = open(f'./DATA/charts/{self.UDBM.USER_ID}_c3.html', 'r', encoding='UTF-8').read().replace(
                'https://assets.pyecharts.org/assets/echarts.min.js', 'echarts.js')
            open(f'./DATA/charts/{self.UDBM.USER_ID}_c3.html', 'w+', encoding='UTF-8').write(_b)

        open('./DATA/charts/echarts.js', 'w+', encoding='UTF-8').write(
            requests.get('https://assets.pyecharts.org/assets/echarts.min.js').text)

        os.remove('./cache/cache.html')

    # def make_calendar(self):  # 构造日历图对象，传入数据类
    #
    #     calendar2021 = pyecharts.charts.Calendar(
    #         init_opts=pyecharts.options.InitOpts(chart_id='calendar2021', width="1160px", height="240px",
    #                                              theme=pyecharts.globals.ThemeType.MACARONS))
    #     calendar2022 = pyecharts.charts.Calendar(
    #         init_opts=pyecharts.options.InitOpts(chart_id='calendar2022', width="1160px", height="240px",
    #                                              theme=pyecharts.globals.ThemeType.MACARONS))
    #     y_data_2021 = []
    #     y_data_2022 = []
    #     for day in self.sever_class.date_all_datalist:
    #         if day[0].split('-')[0] == '2021':
    #             y_data_2021.append(day)
    #         elif day[0].split('-')[0] == '2022':
    #             y_data_2022.append(day)
    #     # print(y_data_2021)
    #     if y_data_2021 != []:
    #         y_data_2021.sort(key=lambda x: x[1], reverse=True)
    #         # print(y_data_2021)
    #         (
    #             calendar2021
    #             .add(
    #                 series_name="2021",
    #                 yaxis_data=y_data_2021,
    #                 calendar_opts=pyecharts.options.CalendarOpts
    #                     (
    #                     pos_left="30",
    #
    #                     range_="2021",
    #                     yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False)
    #                 ),
    #             )
    #             .set_global_opts
    #                 (
    #                 title_opts=pyecharts.options.TitleOpts(pos_left="left", title="祈愿日历"),
    #                 visualmap_opts=pyecharts.options.VisualMapOpts
    #                     (
    #                     max_=y_data_2021[0][1], min_=1, orient="horizontal", is_piecewise=False, pos_left='center'
    #
    #                 )
    #             )
    #         )
    #     if y_data_2022 != []:
    #         y_data_2022.sort(key=lambda x: x[1], reverse=True)
    #
    #         (
    #             calendar2022
    #             .add(
    #                 series_name="2022",
    #                 yaxis_data=y_data_2022,
    #                 calendar_opts=pyecharts.options.CalendarOpts
    #                     (
    #                     pos_left="30",
    #
    #                     range_="2022",
    #                     yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False)
    #                 ),
    #             )
    #             .set_global_opts
    #                 (
    #                 title_opts=pyecharts.options.TitleOpts(pos_left="left", title="祈愿日历"),
    #                 visualmap_opts=pyecharts.options.VisualMapOpts
    #                     (
    #                     max_=y_data_2022[0][1], min_=1, orient="horizontal", is_piecewise=False, pos_left='center'
    #
    #                 )
    #             )
    #         )
    #     if y_data_2021 != [] and y_data_2022 != []:
    #         return calendar2021, calendar2022
    #     elif y_data_2021 == [] and y_data_2022 != []:
    #         return 0, calendar2022
    #     elif y_data_2021 == [] and y_data_2022 == []:
    #         return 0, 0
    #     elif y_data_2021 != [] and y_data_2022 == []:
    #         return calendar2021, 0
    #
    # def make_scatter(self):  # 构造散点图对象，传入数据类
    #
    #     data_3 = self.sever_class.time_all_datalist_3
    #     data_4 = self.sever_class.time_all_datalist_4
    #     data_5 = self.sever_class.time_all_datalist_5
    #     y_data_3 = []
    #     y_data_4 = []
    #     y_data_5 = []
    #
    #     x_data_3 = []
    #     x_data_4 = []
    #     x_data_5 = []
    #
    #     x_data = []
    #     data_3.sort(key=lambda x: x[0])
    #     data_4.sort(key=lambda x: x[0])
    #     data_5.sort(key=lambda x: x[0])
    #     for i in data_3:
    #         x_data_3.append(i[0])
    #         y_data_3.append(i[1])
    #
    #     for i in data_4:
    #         x_data_4.append(i[0])
    #         y_data_4.append(i[1])
    #
    #     for i in data_5:
    #         x_data_5.append(i[0])
    #         y_data_5.append(i[1])
    #
    #     for i in range(24):
    #         if i < 10:
    #             x_data.append('0' + str(i) + ':00')
    #         else:
    #             x_data.append(str(i) + ':00')
    #
    #     scatter = (
    #         pyecharts.charts.Scatter(
    #             init_opts=pyecharts.options.InitOpts(chart_id='出货时间分布', theme=pyecharts.globals.ThemeType.MACARONS))
    #         .add_xaxis(x_data)
    #
    #         # .add_xaxis( x_data_3)
    #         .add_yaxis('三星', y_data_3)
    #         # .add_xaxis(x_data_4)
    #         .add_yaxis('四星', y_data_4)
    #         # .add_xaxis(x_data_5)
    #         .add_yaxis('五星', y_data_5)
    #         .set_global_opts
    #             (
    #             title_opts=pyecharts.options.TitleOpts(title="出货时间分布"),
    #             visualmap_opts=pyecharts.options.VisualMapOpts(type_="size", max_=max(y_data_4 + y_data_5), min_=1)
    #         )
    #     )
    #     scatter.width = '640px'
    #     scatter.height = '480px'
    #
    #     return scatter
