print('''
                    月海仙麟 -- 原神祈愿数据统计 v1.0.1
        作者：南辰燏炚  联系QQ：3546599908  原神交流群：777974176

        github：https://github.com/LingXuanYin/YueHaiXianLin

        bilibili：https://space.bilibili.com/162599415

        使用出现任何问题请直接联系开发者

        本软件禁止任何未授权转载、转发

        请勿删除软件目录下的‘藏弓待用.txt’
        这是您的数据文件
        删除或更改其内容会导致展示数据不准确等错误


        ''')

import os
import sys
import threading
import time
import urllib
import webbrowser

import pyecharts
import requests

import Save

self_path = os.getcwd()


class Tool():  # 工具类函数
    def dict_to_list(self, dict={}):  # 字典转列表
        dictlist = []
        for keys, value in dict.items():
            temp = [keys, value]
            dictlist.append(temp)
        # print(dictlist)
        return dictlist


class Log():  # 日志类

    # 复制日志文件到根目录
    def get_log(self):

        l_path = os.getenv("APPDATA")
        # log_path=input("获取日志目录失败，请手动输入/n 示例:C://Users//Username//AppData//LocalLow//")

        log_path = os.path.join(l_path, "../") + "LocalLow/miHoYo/原神/output_log.txt"
        log_last_path = os.path.join(l_path, "../") + "LocalLow/miHoYo/原神/output_log.txt.last"

        open(self_path + '/output_log.txt', 'w+', encoding='UTF-8').write(
            open(log_path, 'r', encoding='UTF-8').read())

    # 获取初始url
    def get_url(self):
        #
        if os.path.exists(self_path + '/output_log.txt'):
            log = open(self_path + '/output_log.txt', 'r', encoding='UTF-8').read()
        else:
            self.get_log()
            log=open(self_path + '/output_log.txt', 'r', encoding='UTF-8').read()
        start = log.rfind('https://webstatic.mihoyo.com/hk4e/event/')
        end = log.rfind('#/log') + 5
        url = str(log[start:end])
        '''
        url_,request_data=self.trans_url(url, gacha_type, page,endid)

        response_list=request().request(url_, request_data)'''
        return url

    # 处理url，获取认证秘钥等
    def trans_url(self, url_forfirst, gacha_type, page, end_id):
        # print(url_forfirst)
        try:
            authkey_ver = int(url_forfirst[url_forfirst.index('authkey_ver=') + 12])
        except:
            # print("authkey_ver不可用")
            authkey_ver = "1"
        try:
            sign_type = int(url_forfirst[url_forfirst.index('sign_type=') + 10])
        except:
            # print("sign_type不可用")
            sign_type = "2"
        try:
            auth_appid = url_forfirst[url_forfirst.index('auth_appid=') + 11:url_forfirst.index('&init_type')]
        except:
            # print("auth_appid不可用")
            auth_appid = "webview_gacha"
        try:
            init_type = int(url_forfirst[url_forfirst.index('init_type=') + 10:url_forfirst.index('&gacha_id')])
        except:
            # print("init_type不可用")
            init_type = "301"
        try:
            gacha_id = url_forfirst[url_forfirst.index('gacha_id=') + 9:url_forfirst.index('&timestamp')]
        except:  # Exception() as e:
            # open('log.txt', 'a', encoding='utf-8').writelines(str(e))
            raise Exception("gacha_id不可用，请刷新链接")
        try:
            timestamp = int(url_forfirst[url_forfirst.index('timestamp=') + 10:url_forfirst.index('&lang')])
        except:
            # print("timestamp不可用")
            timestamp = int(time.time())  # 使用实时时间
        try:
            device_type = url_forfirst[url_forfirst.index('device_type=') + 12:url_forfirst.index('&ext')]
        except:
            # print("device_type不可用")
            device_type = "pc"
        try:
            game_version = url_forfirst[url_forfirst.index('game_version=') + 13:url_forfirst.index('&plat_type')]
        except:
            raise Exception("game_version不可用，请刷新链接")
        try:
            plat_type = url_forfirst[url_forfirst.index('plat_type=') + 10:url_forfirst.index('&region')]
        except:
            # print("plat_type不可用")
            plat_type = "pc"
        try:
            region = url_forfirst[url_forfirst.index('region=') + 7:url_forfirst.index('&authkey')]
        except:
            # print("authkey_ver不可用")
            region = "cn_gf01"
        try:
            authkey = url_forfirst[url_forfirst.index('authkey=') + 8:url_forfirst.index('&game_biz')]
        except:
            raise Exception("authkey_ver不可用，请刷新链接")
        try:
            game_biz = url_forfirst[url_forfirst.index('game_biz=') + 9:url_forfirst.index('#/log')]
        except:
            # print("game_biz不可用")
            game_biz = "hk4e_cn"

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
            'authkey': urllib.parse.unquote(authkey),
            'game_biz': game_biz,
            'gacha_type': gacha_type,
            'page': page,
            'size': 20,
            'end_id': end_id
        }
        url = '''https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'''
        return url, data


class data():  # 数据类

    date_all_datalist = []  # 总日期
    date_all_data = {}  # 总日期
    time_all_data_3 = {}  # 总时间
    time_all_data_4 = {}  # 总时间
    time_all_data_5 = {}  # 总时间
    time_all_datalist_3 = []  # 总时间
    time_all_datalist_4 = []  # 总时间
    time_all_datalist_5 = []  # 总时间

    class permanent():  # 常驻祈愿
        wap_5 = []
        wap_4 = []
        wap_3 = []
        char_5 = []
        char_4 = []
        total = []

        class time():  # 时间数据
            time_char_5 = []  # 总出货时间
            time_char_4 = []
            time_wap_5 = []
            time_wap_4 = []
            time_wap_3 = []

            # 时间统计
            time_count_all_5 = {}
            time_count_all_4 = {}
            time_count_wap_3 = {}

            time_countlist_all_5 = []
            time_countlist_all_4 = []
            time_countlist_wap_3 = []

        class date():  # 日期数据
            date_char_5 = []  # 总出货日期
            date_char_4 = []
            date_wap_5 = []
            date_wap_4 = []
            date_wap_3 = []

            # 日期统计
            date_count_all_5 = {}
            date_count_all_4 = {}
            date_count_wap_3 = {}

            date_countlist_all_5 = []
            date_countlist_all_4 = []
            date_countlist_wap_3 = []

    class charactivity():  # 角色活动祈愿
        wap_5 = []
        wap_4 = []
        wap_3 = []
        char_5 = []
        char_4 = []
        total = []

        class time():  # 时间数据
            time_char_5 = []  # 总出货时间
            time_char_4 = []
            time_wap_5 = []
            time_wap_4 = []
            time_wap_3 = []

            # 时间统计
            time_count_all_5 = {}
            time_count_all_4 = {}
            time_count_wap_3 = {}

            time_countlist_all_5 = []
            time_countlist_all_4 = []
            time_countlist_wap_3 = []

        class date():  # 日期数据
            date_char_5 = []  # 总出货日期
            date_char_4 = []
            date_wap_5 = []
            date_wap_4 = []
            date_wap_3 = []

            # 日期统计
            date_count_all_5 = {}
            date_count_all_4 = {}
            date_count_wap_3 = {}

            date_countlist_all_5 = []
            date_countlist_all_4 = []
            date_countlist_wap_3 = []

    class wapactivity():  # 武器活动祈愿
        wap_5 = []
        wap_4 = []
        wap_3 = []
        char_5 = []
        char_4 = []
        total = []

        class time():  # 时间数据
            time_char_5 = []  # 总出货时间
            time_char_4 = []
            time_wap_5 = []
            time_wap_4 = []
            time_wap_3 = []

            # 时间统计
            time_count_all_5 = {}
            time_count_all_4 = {}
            time_count_wap_3 = {}

            time_countlist_all_5 = []
            time_countlist_all_4 = []
            time_countlist_wap_3 = []

        class date():  # 日期数据
            date_char_5 = []  # 总出货日期
            date_char_4 = []
            date_wap_5 = []
            date_wap_4 = []
            date_wap_3 = []

            # 日期统计
            date_count_all_5 = {}
            date_count_all_4 = {}
            date_count_wap_3 = {}

            date_countlist_all_5 = []
            date_countlist_all_4 = []
            date_countlist_wap_3 = []

    class novice():  # 新手祈愿
        wap_5 = []
        wap_4 = []
        wap_3 = []
        char_5 = []
        char_4 = []
        total = []

        class time():  # 时间数据
            time_char_5 = []  # 总出货时间
            time_char_4 = []
            time_wap_5 = []
            time_wap_4 = []
            time_wap_3 = []

            # 时间统计
            time_count_all_5 = {}
            time_count_all_4 = {}
            time_count_wap_3 = {}

            time_countlist_all_5 = []
            time_countlist_all_4 = []
            time_countlist_wap_3 = []

        class date():  # 日期数据
            date_char_5 = []  # 总出货日期
            date_char_4 = []
            date_wap_5 = []
            date_wap_4 = []
            date_wap_3 = []

            # 日期统计
            date_count_all_5 = {}
            date_count_all_4 = {}
            date_count_wap_3 = {}

            date_countlist_all_5 = []
            date_countlist_all_4 = []
            date_countlist_wap_3 = []

    class_list = [wapactivity(), charactivity(), permanent(), novice()]

    def ensure_count_process(self):  # 保底计数处理
        for class_ in self.class_list:
            ensure_count = 0
            ensure_buf5, ensure_buf4 = 0, 0
            for sth in class_.total:
                ensure_count += 1
                sth['ensure_count'] = ensure_count - ensure_buf5
                sth['ensure_4'] = ensure_count - ensure_buf4
                if sth['rank_type'] == '5':
                    ensure_buf5 = ensure_count
                if sth['rank_type'] == '4':
                    ensure_buf4 = ensure_count

    def datetimedata_process(self):  # 数据日期时间处理
        for class_ in self.class_list:
            # 处理四星出货时间
            for time in class_.time().time_char_4 + class_.time().time_wap_4:
                if time not in class_.time().time_count_all_4.keys():
                    class_.time().time_count_all_4[time] = 1
                else:
                    class_.time().time_count_all_4[time] += 1
            class_.time().time_countlist_all_4 += sorted(Tool().dict_to_list(class_.time().time_count_all_4),
                                                         key=lambda x: x[0])

            # 处理五星出货时间
            for time in class_.time().time_char_5 + class_.time().time_wap_5:
                if time not in class_.time().time_count_all_5.keys():
                    class_.time().time_count_all_5[time] = 1
                else:
                    class_.time().time_count_all_5[time] += 1
            class_.time().time_countlist_all_5 += sorted(Tool().dict_to_list(class_.time().time_count_all_5),
                                                         key=lambda x: x[0])
            # 处理三星出货时间
            for time in class_.time().time_wap_3:
                if time not in class_.time().time_count_wap_3.keys():
                    class_.time().time_count_wap_3[time] = 1
                else:
                    class_.time().time_count_wap_3[time] += 1
            class_.time().time_countlist_wap_3 += sorted(Tool().dict_to_list(class_.time().time_count_wap_3),
                                                         key=lambda x: x[0])
            # 处理四星出货日期
            for date in class_.date().date_char_4 + class_.date().date_wap_4:
                if date not in class_.date().date_count_all_4.keys():
                    class_.date().date_count_all_4[date] = 1
                else:
                    class_.date().date_count_all_4[date] += 1
            class_.date().date_countlist_all_4 += sorted(Tool().dict_to_list(class_.date().date_count_all_4),
                                                         key=lambda x: x[0])
            # 处理五星出货日期

            for date in class_.date().date_char_5 + class_.date().date_wap_5:

                if date not in class_.date().date_count_all_5.keys():
                    class_.date().date_count_all_5[date] = 1
                else:
                    class_.date().date_count_all_5[date] += 1
            class_.date().date_countlist_all_5 += sorted(Tool().dict_to_list(class_.date().date_count_all_5),
                                                         key=lambda x: x[0])
            # 处理三星出货日期
            for date in class_.date().date_wap_3:
                if date not in class_.date().date_count_wap_3.keys():
                    class_.date().date_count_wap_3[date] = 1
                else:
                    class_.date().date_count_wap_3[date] += 1
            class_.date().date_countlist_wap_3 += sorted(Tool().dict_to_list(class_.date().date_count_wap_3),
                                                         key=lambda x: x[0])
        for class_ in data().class_list:  # 处理总计数
            # 处理四星出货时间
            for time in class_.time().time_count_all_4.keys():
                if time not in data().time_all_data_4.keys():
                    data().time_all_data_4[time] = class_.time().time_count_all_4[time]
                else:
                    data().time_all_data_4[time] += class_.time().time_count_all_4[time]

            # 处理五星出货时间
            for time in class_.time().time_count_all_5.keys():
                if time not in data().time_all_data_5.keys():
                    data().time_all_data_5[time] = class_.time().time_count_all_5[time]
                else:
                    data().time_all_data_5[time] += class_.time().time_count_all_5[time]

            # 处理三星出货时间
            for time in class_.time().time_count_wap_3.keys():
                if time not in data().time_all_data_3.keys():
                    data().time_all_data_3[time] = class_.time().time_count_wap_3[time]
                else:
                    data().time_all_data_3[time] += class_.time().time_count_wap_3[time]

            # 处理四星出货日期
            for date in class_.date().date_count_all_4.keys():
                if date not in data().date_all_data.keys():
                    data().date_all_data[date] = class_.date().date_count_all_4[date]
                else:
                    data().date_all_data[date] += class_.date().date_count_all_4[date]

            # 处理五星出货日期
            for date in class_.date().date_count_all_5.keys():
                if date not in data().date_all_data.keys():
                    data().date_all_data[date] = class_.date().date_count_all_5[date]
                else:
                    data().date_all_data[date] += class_.date().date_count_all_5[date]
            # 处理三星出货日期
            for date in class_.date().date_count_wap_3.keys():
                if date not in data().date_all_data.keys():
                    data().date_all_data[date] = class_.date().date_count_wap_3[date]
                else:
                    data().date_all_data[date] += class_.date().date_count_wap_3[date]

        data().date_all_datalist += sorted(Tool().dict_to_list(data().date_all_data), key=lambda x: x[0])
        data().time_all_datalist_3 += sorted(Tool().dict_to_list(data().time_all_data_3), key=lambda x: x[0])
        data().time_all_datalist_4 += sorted(Tool().dict_to_list(data().time_all_data_4), key=lambda x: x[0])
        data().time_all_datalist_5 += sorted(Tool().dict_to_list(data().time_all_data_5), key=lambda x: x[0])

    def maindata_process(self):  # 数据分类
        for class_ in self.class_list:
            for sth in class_.total:
                if sth['rank_type'] == '3':
                    class_.wap_3.append(sth)
                    class_.date().date_wap_3.append(sth['time'].split(' ')[0])
                    class_.time().time_wap_3.append(sth['time'].split(' ')[1].split(':')[0])
                elif sth['rank_type'] == '4':
                    if sth['item_type'] == '角色':
                        class_.char_4.append(sth)
                        class_.date().date_char_4.append(sth['time'].split(' ')[0])
                        class_.time().time_char_4.append(sth['time'].split(' ')[1].split(':')[0])
                    elif sth['item_type'] == '武器':
                        class_.wap_4.append(sth)
                        class_.date().date_wap_4.append(sth['time'].split(' ')[0])
                        class_.time().time_wap_4.append(sth['time'].split(' ')[1].split(':')[0])
                elif sth['rank_type'] == '5':
                    if sth['item_type'] == '角色':
                        class_.char_5.append(sth)
                        class_.date().date_char_5.append(sth['time'].split(' ')[0])
                        class_.time().time_char_5.append(sth['time'].split(' ')[1].split(':')[0])
                    elif sth['item_type'] == '武器':
                        class_.wap_5.append(sth)
                        class_.date().date_wap_5.append(sth['time'].split(' ')[0])
                        class_.time().time_wap_5.append(sth['time'].split(' ')[1].split(':')[0])

    def merge_data(self, read_data):  # 新旧数据混合
        for sth in read_data:
            if sth not in self.charactivity().total and (sth['gacha_type'] == '301' or sth['gacha_type'] == '400'):
                self.charactivity().total.append(sth)
            if sth not in self.wapactivity().total and sth['gacha_type'] == '302':
                self.wapactivity().total.append(sth)
            if sth not in self.permanent().total and sth['gacha_type'] == '200':
                self.permanent().total.append(sth)
            if sth not in self.novice().total and sth['gacha_type'] == '100':
                self.novice().total.append(sth)
        self.ensure_count_process()  # 混合完成直接添加保底计数

    def request_data_processor(self, src_data, gacha_type):  # 数据初步分类
        if src_data == []:
            {}  # 跳过空列表
        elif gacha_type == 400 or gacha_type == 301:  # 角色活动祈愿
            self.charactivity().total += (src_data)
            # print(self.charactivity().total)
            # self.charactivity().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 302:  # 武器活动祈愿
            self.wapactivity().total += (src_data)
            # self.wapactivity().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 200:  # 常驻祈愿
            self.permanent().total += (src_data)
            # self.permanent().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 100:  # 新手祈愿
            self.novice().total += (src_data)
            # self.novice().total.sort(key=operator.itemgetter('id'),reverse = True)
        # print(src_data)
        # print(self.charactivity().total)

    def make_detail(self, data_class):  # 构造具体数据展示字符串，传入数据类，返回：三星武器计数，四星人物detail，四星武器detail，五星人物detail，五星武器detail
        total_str_5 = ''  # 五星不分开展示，使用一个字符串
        char_str_4 = ''
        wap_str_4 = ''
        wap_str_3 = ''
        wap3_count = {}
        wap3_countlist = []
        ensure_count_buf = 0
        list_buf_5, list_buf_4 = [], []
        # 集合五星数据
        for sth in data_class.total:
            if sth['rank_type'] == '5':
                list_buf_5.append(sth)
            if sth['rank_type'] == '4':
                list_buf_4.append(sth)
        for sth in list_buf_5:
            ensure_count_buf += sth['ensure_count']

        for w3 in data_class.wap_3:  # 统计三星武器并排序
            if w3['name'] not in wap3_count.keys():
                wap3_count[w3['name']] = 1
            else:
                wap3_count[w3['name']] += 1
        wap3_countlist = sorted(Tool().dict_to_list(wap3_count), key=lambda x: x[1], reverse=True)

        for i in range(len(wap3_countlist)):  # 生成三星武器统计数据字符串
            if i % 3 == 0 and i != 0:
                wap_str_3 += '</br> '
            wap_str_3 += (' ' + wap3_countlist[i][0] + '[' + str(wap3_countlist[i][1]) + '] ')
        # print(wap_str_3)
        for i in range(len(list_buf_4)):  # 生成四星人物统计数据字符串
            if i % 3 == 0 and i != 0:
                char_str_4 += '</br> '
            char_str_4 += ('[' + str(list_buf_4[i]['ensure_4'] - 1) + ']-- ' + list_buf_4[i]['name'] + ' --')

        for i in range(len(list_buf_4)):  # 生成四星武器统计数据字符串
            if i % 3 == 0 and i != 0:
                wap_str_4 += '</br> '
            wap_str_4 += ('[' + str(list_buf_4[i]['ensure_4'] - 1) + ']-- ' + list_buf_4[i]['name'] + ' --')

        for i in range(len(list_buf_5)):  # 生成五星统计数据字符串
            if i % 3 == 0 and i != 0:
                total_str_5 += '</br> '
            total_str_5 += ('[' + str(list_buf_5[i]['ensure_count'] - 1) + ']-- ' + list_buf_5[i]['name'] + ' --')
        total_str_5 += '[' + str(len(data_class.total) - ensure_count_buf) + ']'
        return wap_str_3, char_str_4, wap_str_4, total_str_5, total_str_5


class charts():  # 图表类
    def make_pie(self, data_class):  # 构造饼图对象，传入数据类
        wap3, char4, wap4, char5, wap5 = data().make_detail(data_class)
        total_count = 0
        data_ = [['三星', len(data_class.wap_3)], ['四星武器', len(data_class.wap_4)], ['四星角色', len(data_class.char_4)],
                 ['五星武器', len(data_class.wap_5)], ['五星角色', len(data_class.char_5)]]
        for i in data_:
            total_count += i[1]
        gacha_type = data_class.total[0]['gacha_type']
        if (gacha_type == '200'):  # 常驻祈愿
            charts_name = '''常驻祈愿'''

        elif (gacha_type == '100'):  # 新手祈愿
            charts_name = ''' 新手祈愿'''

        elif (gacha_type == '301' or gacha_type == '400'):  # 角色活动祈愿
            charts_name = '''角色活动祈愿'''

        elif (gacha_type == '302'):  # 武器活动祈愿
            charts_name = '''武器活动祈愿'''

        # if total_count == 0:total_count=1
        pie = (
            pyecharts.charts.Pie(init_opts=pyecharts.options.InitOpts(chart_id=charts_name,
                                                                      theme=pyecharts.globals.ThemeType.MACARONS))  # 设置id和主题
                .add(
                charts_name,
                data_,

                tooltip_opts=pyecharts.options.TooltipOpts
                    (
                    border_color='red',
                    border_width='1',
                    trigger_on='mousemove|click',
                    formatter=pyecharts.globals.JsCode('''function(parg){\n
                    if( parg.name == '三星')\n
                    {\n
                    return ' 三星： ''' + str(len(data_class.wap_3)) + ' ( ' + str(
                        int((len(data_class.wap_3) / total_count) * 10000) / 100) + ''' % )</br>'+\'''' + wap3 + '''\' ;\n


                    }else if (parg.name == '四星武器')\n
                    {\n
                    return ' 四星武器： ''' + str(len(data_class.wap_4) + len(data_class.char_4)) + ' ( ' + str(int(((
                                                                                                                                                                                                                                             len(data_class.wap_4) + len(
                                                                                                                                                                                                                                         data_class.char_4)) / total_count) * 10000) / 100) + ''' % )</br>'+\'''' + wap4 + '''\' ;\n

                    }else if (parg.name == '五星武器')\n
                    {\n
                    return ' 五星： ''' + str(len(data_class.wap_5) + len(data_class.char_5)) + ' ( ' + str(int(((
                                                                                                                                                                                                                                                                                                                                                                                                                                                     len(data_class.wap_5) + len(
                                                                                                                                                                                                                                                                                                                                                                                                                                                 data_class.char_5)) / total_count) * 10000) / 100) + ''' % )</br>'+\'''' + wap5 + '''\' ;\n

                    }else if (parg.name == '四星角色')\n
                    {\n
                    return ' 四星角色： ''' + str(len(data_class.wap_4) + len(data_class.char_4)) + ' ( ' + str(int(((
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               len(data_class.wap_4) + len(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           data_class.char_4)) / total_count) * 10000) / 100) + ''' % )</br>'+\'''' + char4 + '''\' ;\n

                    }else if (parg.name == '五星角色')\n
                    {\n
                    return ' 五星： ''' + str(len(data_class.wap_5) + len(data_class.char_5)) + ' ( ' + str(int(((
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        len(data_class.wap_5) + len(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    data_class.char_5)) / total_count) * 10000) / 100) + ''' % )</br>'+\'''' + char5 + '''\' ;\n

                    }\n
                }\n
                                                   '''),
                    textstyle_opts=pyecharts.options.TextStyleOpts(font_size=16)
                    # 添加JS回调函数使数据随鼠标指向的图表变动，展示具体记录

                ),

                radius=["35%", "70%"],

            )
                .set_global_opts(title_opts=pyecharts.options.TitleOpts(charts_name))
        ).add_js_funcs('''
                       option_defult = {

            series: [
                {type:'pie',
                    name:''' + charts_name + ''',

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
                       }]};
                       chart_''' + charts_name + '''.setOption(option_defult);''')

        pie.width = '720px'
        pie.height = '540px'
        # 保存格式化之后的数据
        return pie

    def make_calendar(self):  # 构造日历图对象，传入数据类

        calendar2021 = pyecharts.charts.Calendar(
            init_opts=pyecharts.options.InitOpts(chart_id='calendar2021', width="1160px", height="240px",
                                                 theme=pyecharts.globals.ThemeType.MACARONS))
        calendar2022 = pyecharts.charts.Calendar(
            init_opts=pyecharts.options.InitOpts(chart_id='calendar2022', width="1160px", height="240px",
                                                 theme=pyecharts.globals.ThemeType.MACARONS))
        y_data_2021 = []
        y_data_2022 = []
        for day in data().date_all_datalist:
            if day[0].split('-')[0] == '2021':
                y_data_2021.append(day)
            elif day[0].split('-')[0] == '2022':
                y_data_2022.append(day)
        # print(y_data_2021)
        if y_data_2021 != []:
            y_data_2021.sort(key=lambda x: x[1], reverse=True)
            # print(y_data_2021)
            (
                calendar2021
                    .add(
                    series_name="2021",
                    yaxis_data=y_data_2021,
                    calendar_opts=pyecharts.options.CalendarOpts
                        (
                        pos_left="30",

                        range_="2021",
                        yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False)
                    ),
                )
                    .set_global_opts
                    (
                    title_opts=pyecharts.options.TitleOpts(pos_left="left", title="抽卡分布"),
                    visualmap_opts=pyecharts.options.VisualMapOpts
                        (
                        max_=y_data_2021[0][1], min_=1, orient="horizontal", is_piecewise=False, pos_left='center'

                    )
                )
            )
        if y_data_2022 != []:
            y_data_2022.sort(key=lambda x: x[1], reverse=True)

            (
                calendar2022
                    .add(
                    series_name="2022",
                    yaxis_data=y_data_2022,
                    calendar_opts=pyecharts.options.CalendarOpts
                        (
                        pos_left="30",

                        range_="2022",
                        yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False)
                    ),
                )
                    .set_global_opts
                    (
                    title_opts=pyecharts.options.TitleOpts(pos_left="left", title="抽卡分布"),
                    visualmap_opts=pyecharts.options.VisualMapOpts
                        (
                        max_=y_data_2022[0][1], min_=1, orient="horizontal", is_piecewise=False, pos_left='center'

                    )
                )
            )
        if y_data_2021 != [] and y_data_2022 != []:
            return calendar2021, calendar2022
        elif y_data_2021 == [] and y_data_2022 != []:
            return 0, calendar2022
        elif y_data_2021 == [] and y_data_2022 == []:
            return 0, 0
        elif y_data_2021 != [] and y_data_2022 == []:
            return calendar2021, 0

    def make_scatter(self):  # 构造散点图对象，传入数据类

        data_3 = data().time_all_datalist_3
        data_4 = data().time_all_datalist_4
        data_5 = data().time_all_datalist_5
        y_data_3 = []
        y_data_4 = []
        y_data_5 = []

        x_data_3 = []
        x_data_4 = []
        x_data_5 = []

        x_data = []
        data_3.sort(key=lambda x: x[0])
        data_4.sort(key=lambda x: x[0])
        data_5.sort(key=lambda x: x[0])
        for i in data_3:
            x_data_3.append(i[0])
            y_data_3.append(i[1])

        for i in data_4:
            x_data_4.append(i[0])
            y_data_4.append(i[1])

        for i in data_5:
            x_data_5.append(i[0])
            y_data_5.append(i[1])

        for i in range(24):
            if i < 10:
                x_data.append('0' + str(i) + ':00')
            else:
                x_data.append(str(i) + ':00')

        scatter = (
            pyecharts.charts.Scatter(
                init_opts=pyecharts.options.InitOpts(chart_id='出货时间分布', theme=pyecharts.globals.ThemeType.MACARONS))
                .add_xaxis(x_data)

                # .add_xaxis( x_data_3)
                .add_yaxis('三星', y_data_3)
                # .add_xaxis(x_data_4)
                .add_yaxis('四星', y_data_4)
                # .add_xaxis(x_data_5)
                .add_yaxis('五星', y_data_5)
                .set_global_opts
                (
                title_opts=pyecharts.options.TitleOpts(title="出货时间分布"),
                visualmap_opts=pyecharts.options.VisualMapOpts(type_="size", max_=max(y_data_4 + y_data_5), min_=1)
            )
        )
        scatter.width = '640px'
        scatter.height = '480px'

        return scatter

    def draw_charts(self):  # 绘制所有图表对象
        page = pyecharts.charts.Page(page_title='山泽麟迹', layout=pyecharts.charts.Page.DraggablePageLayout)

        if data().charactivity().total != []:
            pie_char = self.make_pie(data().charactivity())
            page.add(pie_char)
        else:
            pie_char = 0
            print("角色活动祈愿为空")

        if data().wapactivity().total != []:
            pie_wap = self.make_pie(data().wapactivity())
            page.add(pie_wap)
        else:
            pie_wap = 0
            print("武器活动祈愿为空")

        if data().permanent().total != []:
            pie_per = self.make_pie(data().permanent())
            page.add(pie_per)

        else:
            pie_per = 0
            print("常驻祈愿为空")

        if data().novice().total != []:
            pie_nov = self.make_pie(data().novice())
            page.add(pie_nov)
        else:
            pie_nov = 0
            print("新手祈愿为空")

        scatter = self.make_scatter()
        page.add(scatter)
        calendar2021, calendar2022 = self.make_calendar()

        # page.add(pie1,pie2,pie3).render('TEST.html')#添加图表,不含日历图
        if calendar2021 != 0:
            page.add(calendar2021)
        else:
            print("2021 data not found")
        if calendar2022 != 0:
            page.add(calendar2022)
        else:
            print("2022 data not found")
        page.render(self_path + '/TEST.html')
        page.save_resize_html(self_path + '/TEST.html', cfg_file=self_path + '/chart_config.json',
                              dest=self_path + '/山泽麟迹.html')
        os.remove(self_path + '/TEST.html')
        # 需要改变图表布局则屏蔽这两行，在测试网页里保存配置(*.json)，或者直接修改


class request():  # 请求数据

    def get_srcdata(self, gacha_type):
        page, endid = 1, 0
        src_url = Log().get_url()
        while True:
            url, request_data = Log().trans_url(src_url, gacha_type, page, endid)

            response_list = self.request(url, request_data)
            if response_list == []: break  # 无数据提前跳出
            if response_list == 'visit too frequently':
                continue  # 防止请求频繁
            else:
                for sth in response_list:
                    sth['id'] = int(sth['id'])
                data().request_data_processor(response_list, gacha_type)  # 送至处理函数
            if len(response_list) != 20: break  # 最后一页跳出
            # 处理结束ID
            endid = response_list[len(response_list) - 1]['id']

            # 处理页数

            if (gacha_type == 200):  # 常驻祈愿
                print("获取 常驻祈愿 " + str(page) + ' 页')

            elif (gacha_type == 100):  # 新手祈愿
                print("获取 新手祈愿 " + str(page) + ' 页')

            elif (gacha_type == 301 or gacha_type == 400):  # 角色活动祈愿
                print("获取 角色活动祈愿 " + str(page) + ' 页')

            elif (gacha_type == 302):  # 武器活动祈愿
                print("获取 武器活动祈愿 " + str(page) + ' 页')

            page += 1

    def request(self, src_url, src_data):
        src_data['timestamp'] = int(time.time())  # 使用实时时间
        response = requests.get(src_url, src_data)
        # print(response.text)
        try:
            if (response.text.index('visit too frequently')):
                time.sleep(0.5)  # 防止请求频繁
                return 'visit too frequently'
        except:
            {}

        if 'null' in response.text:
            #os.remove(self_path + '/output_log.txt')

            if (os.path.exists('ERRORFLAG')):
                raise Exception(str(src_data['gacha_type']) + ' ' + response.text[24:39] + '\n请登录 原神->祈愿->历史记录 刷新链接后重试')
            else:
                open('ERRORFLAG','w+').close()
                print('\nURL Error or Exceed the Time Limit\n\nRetry...\n')
                time.sleep(3)
                main()

        return eval(response.text)['data']['list']


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():

    # 初始化资源文件
    print("\nLoading...\n")
    time.sleep(3)
    os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), "cacert.pem")
    file_json = resource_path(os.path.join("res", "chart_config.json"))
    file_dem = resource_path(os.path.join("res", "cacert.pem"))
    open(self_path + "/cacert.pem", 'w+').write(open(file_dem, 'r+').read())
    open(self_path + "/chart_config.json", 'w+').write(open(file_json, 'r+').read())
    if not os.path.exists('chart_config.json'):
        open("chart_config.json", 'w+').writelines(open(file_json, 'r+', encoding='utf-8').read())

    print('Checking URL...\n')
    try:
        page, endid = 1, 0
        src_url = Log().get_url()
        url, request_data = Log().trans_url(src_url, 301, page, endid)

        response_list =request(). request(url, request_data)
        print('URL correct !\n')
    except  Exception as e:
        os.remove(self_path + '/output_log.txt')

        if (os.path.exists('ERRORFLAG')):
            raise Exception('\n请登录 原神->祈愿->历史记录 刷新链接后重试\n')
        else:
            open('ERRORFLAG','w+').close()
            print('\nURL Error or Exceed the Time Limit\n\nRetry...\n')
            time.sleep(3)
            main()


    print("Getting data from miHoYo API with 4 threads...\n")
    thread_301 = threading.Thread(target=request().get_srcdata, args=(301,))
    thread_302 = threading.Thread(target=request().get_srcdata, args=(302,))
    thread_200 = threading.Thread(target=request().get_srcdata, args=(200,))
    thread_100 = threading.Thread(target=request().get_srcdata, args=(100,))
    thread_301.start()
    thread_302.start()
    thread_200.start()
    thread_100.start()
    while True:
        # time.sleep(0.5)
        if len(threading.enumerate()) == 1: break

    print('Saving data...\n')
    Save.Save_all_data(
        data().charactivity().total + data().wapactivity().total + data().permanent().total + data().novice().total)  # 调用Save保存数据到对应文件
    print('Saving success !\n')
    print('Merging...')
    data().merge_data(Save.Read_all_data(data().charactivity().total[0]['uid']))  # 调用Save读取对应uid数据文件中的数据
    print("Merge success !\n")
    print("Processing main-data...\n")
    data().maindata_process()
    print("Success !\n")
    print("Processing time...\n")
    data().datetimedata_process()
    print('Success !\n')
    print("Drawing...\n")
    charts().draw_charts()
    print('Success !\n')

    webbrowser.open(self_path + "/山泽麟迹.html")

    if os.path.exists('ERRORFLAG'): os.remove('ERRORFLAG')

    print('Exit...')
    time.sleep(5)
    os.system('taskkill /pid ' + str(os.getpid()) + ' /f')


try:
    main()
except Exception as e:
    print('\nUnexcept Error : \n')
    print(e)
    print('\nExit in 10 sec')
    if os.path.exists('ERRORFLAG'): os.remove('ERRORFLAG')

    time.sleep(10)
    os.system('taskkill /pid ' + str(os.getpid()) + ' /f')
