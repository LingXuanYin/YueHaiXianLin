# coding=utf-8

print('''
                              月海仙麟 -- 原神祈愿数据统计 v1.1.0

                    作者：南辰燏炚  联系QQ：3546599908  原神交流群：777974176

                    github：https://github.com/LingXuanYin/YueHaiXianLin

                    bilibili：https://space.bilibili.com/162599415

                    使用出现任何问题请直接联系开发者

                    本软件禁止任何未授权转载、转发

                    请勿删除软件目录下的‘藏弓待用.txt’
                    这是您的数据文件
                    删除或更改其内容会导致展示数据不准确等错误

        1.1.0已支持国际服
            自动检测是否存在有效链接，同时爬取国服和国际服
            每次仅支持两个不同服务器的uid
            后续会支持多个账号

        ''')

import glob
import os
import sys
import threading
import time as t
import urllib
import webbrowser

import pyecharts
import requests


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def Initialization():
    global l_path, log_path_in, log_path_out, self_path, URL
    # 初始化资源文件
    print("\nLoading...")
    t.sleep(3)
    self_path = os.getcwd()  # 获取运行目录
    # print(self_path)
    l_path = os.getenv("APPDATA")  # 获取日志目录
    # print(l_path)
    log_path_in = os.path.join(l_path, "../LocalLow/miHoYo/原神/output_log.txt")  # 国服日志
    log_path_out = os.path.join(l_path, "../LocalLow/miHoYo/Genshin Impact/output_log.txt")  # 国际服日志

    os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), "cacert.pem")  # 释放资源
    file_json = resource_path(os.path.join("res", "chart_config.json"))
    file_dem = resource_path(os.path.join("res", "cacert.pem"))
    open(self_path + "/cacert.pem", 'w+').write(open(file_dem, 'r+').read())
    if not os.path.exists(self_path + "/chart_config.json"):
        open(self_path + "/chart_config.json", 'w+').writelines(open(file_json, 'r+', encoding='UTF-8').read())
    # 释放完成
    print("\nInitialize success")
    return 1


class data():  # 数据类
    def __init__(self):
        self.ALL_DATA = []

        self.date_all_datalist = []  # 总日期

        self.date_all_data = {}  # 总日期
        self.time_all_data_3 = {}  # 总时间
        self.time_all_data_4 = {}  # 总时间
        self.time_all_data_5 = {}  # 总时间

        self.time_all_datalist_3 = []  # 总时间
        self.time_all_datalist_4 = []  # 总时间
        self.time_all_datalist_5 = []  # 总时间
        self.wapactivity = self.wapactivity()
        self.charactivity = self.charactivity()
        self.permanent = self.permanent()
        self.novice = self.novice()
        self.class_list = [self.wapactivity, self.charactivity, self.permanent, self.novice]

    class permanent():  # 常驻祈愿
        def __init__(self):
            self.wap_5 = []
            self.wap_4 = []
            self.wap_3 = []
            self.char_5 = []
            self.char_4 = []
            self.total = []
            self.time = self.time()
            self.date = self.date()

        class time():  # 时间数据
            def __init__(self):
                self.time_char_5 = []  # 总出货时间
                self.time_char_4 = []
                self.time_wap_5 = []
                self.time_wap_4 = []
                self.time_wap_3 = []

                # 时间统计
                self.time_count_all_5 = {}
                self.time_count_all_4 = {}
                self.time_count_wap_3 = {}

                self.time_countlist_all_5 = []
                self.time_countlist_all_4 = []
                self.time_countlist_wap_3 = []

        class date():  # 日期数据
            def __init__(self):
                self.date_char_5 = []  # 总出货日期
                self.date_char_4 = []
                self.date_wap_5 = []
                self.date_wap_4 = []
                self.date_wap_3 = []

                # 日期统计
                self.date_count_all_5 = {}
                self.date_count_all_4 = {}
                self.date_count_wap_3 = {}

                self.date_countlist_all_5 = []
                self.date_countlist_all_4 = []
                self.date_countlist_wap_3 = []

    class charactivity():  # 角色活动祈愿
        def __init__(self):
            self.wap_5 = []
            self.wap_4 = []
            self.wap_3 = []
            self.char_5 = []
            self.char_4 = []
            self.total = []
            self.time = self.time()
            self.date = self.date()

        class time():  # 时间数据
            def __init__(self):
                self.time_char_5 = []  # 总出货时间
                self.time_char_4 = []
                self.time_wap_5 = []
                self.time_wap_4 = []
                self.time_wap_3 = []

                # 时间统计
                self.time_count_all_5 = {}
                self.time_count_all_4 = {}
                self.time_count_wap_3 = {}

                self.time_countlist_all_5 = []
                self.time_countlist_all_4 = []
                self.time_countlist_wap_3 = []

        class date():  # 日期数据
            def __init__(self):
                self.date_char_5 = []  # 总出货日期
                self.date_char_4 = []
                self.date_wap_5 = []
                self.date_wap_4 = []
                self.date_wap_3 = []

                # 日期统计
                self.date_count_all_5 = {}
                self.date_count_all_4 = {}
                self.date_count_wap_3 = {}

                self.date_countlist_all_5 = []
                self.date_countlist_all_4 = []
                self.date_countlist_wap_3 = []

    class wapactivity():  # 武器活动祈愿
        def __init__(self):
            self.wap_5 = []
            self.wap_4 = []
            self.wap_3 = []
            self.char_5 = []
            self.char_4 = []
            self.total = []
            self.time = self.time()
            self.date = self.date()

        class time():  # 时间数据
            def __init__(self):
                self.time_char_5 = []  # 总出货时间
                self.time_char_4 = []
                self.time_wap_5 = []
                self.time_wap_4 = []
                self.time_wap_3 = []

                # 时间统计
                self.time_count_all_5 = {}
                self.time_count_all_4 = {}
                self.time_count_wap_3 = {}

                self.time_countlist_all_5 = []
                self.time_countlist_all_4 = []
                self.time_countlist_wap_3 = []

        class date():  # 日期数据
            def __init__(self):
                self.date_char_5 = []  # 总出货日期
                self.date_char_4 = []
                self.date_wap_5 = []
                self.date_wap_4 = []
                self.date_wap_3 = []

                # 日期统计
                self.date_count_all_5 = {}
                self.date_count_all_4 = {}
                self.date_count_wap_3 = {}

                self.date_countlist_all_5 = []
                self.date_countlist_all_4 = []
                self.date_countlist_wap_3 = []

    class novice():  # 新手祈愿
        def __init__(self):
            self.wap_5 = []
            self.wap_4 = []
            self.wap_3 = []
            self.char_5 = []
            self.char_4 = []
            self.total = []
            self.time = self.time()
            self.date = self.date()

        class time():  # 时间数据
            def __init__(self):
                self.time_char_5 = []  # 总出货时间
                self.time_char_4 = []
                self.time_wap_5 = []
                self.time_wap_4 = []
                self.time_wap_3 = []

                # 时间统计
                self.time_count_all_5 = {}
                self.time_count_all_4 = {}
                self.time_count_wap_3 = {}

                self.time_countlist_all_5 = []
                self.time_countlist_all_4 = []
                self.time_countlist_wap_3 = []

        class date():  # 日期数据
            def __init__(self):
                self.date_char_5 = []  # 总出货日期
                self.date_char_4 = []
                self.date_wap_5 = []
                self.date_wap_4 = []
                self.date_wap_3 = []

                # 日期统计
                self.date_count_all_5 = {}
                self.date_count_all_4 = {}
                self.date_count_wap_3 = {}

                self.date_countlist_all_5 = []
                self.date_countlist_all_4 = []
                self.date_countlist_wap_3 = []

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
            for time in class_.time.time_char_4 + class_.time.time_wap_4:
                if time not in class_.time.time_count_all_4.keys():
                    class_.time.time_count_all_4[time] = 1
                else:
                    class_.time.time_count_all_4[time] += 1
            class_.time.time_countlist_all_4 += sorted(Tool().dict_to_list(class_.time.time_count_all_4),
                                                       key=lambda x: x[0])

            # 处理五星出货时间
            for time in class_.time.time_char_5 + class_.time.time_wap_5:
                if time not in class_.time.time_count_all_5.keys():
                    class_.time.time_count_all_5[time] = 1
                else:
                    class_.time.time_count_all_5[time] += 1
            class_.time.time_countlist_all_5 += sorted(Tool().dict_to_list(class_.time.time_count_all_5),
                                                       key=lambda x: x[0])
            # 处理三星出货时间
            for time in class_.time.time_wap_3:
                if time not in class_.time.time_count_wap_3.keys():
                    class_.time.time_count_wap_3[time] = 1
                else:
                    class_.time.time_count_wap_3[time] += 1
            class_.time.time_countlist_wap_3 += sorted(Tool().dict_to_list(class_.time.time_count_wap_3),
                                                       key=lambda x: x[0])
            # 处理四星出货日期
            for date in class_.date.date_char_4 + class_.date.date_wap_4:
                if date not in class_.date.date_count_all_4.keys():
                    class_.date.date_count_all_4[date] = 1
                else:
                    class_.date.date_count_all_4[date] += 1
            class_.date.date_countlist_all_4 += sorted(Tool().dict_to_list(class_.date.date_count_all_4),
                                                       key=lambda x: x[0])
            # 处理五星出货日期

            for date in class_.date.date_char_5 + class_.date.date_wap_5:

                if date not in class_.date.date_count_all_5.keys():
                    class_.date.date_count_all_5[date] = 1
                else:
                    class_.date.date_count_all_5[date] += 1
            class_.date.date_countlist_all_5 += sorted(Tool().dict_to_list(class_.date.date_count_all_5),
                                                       key=lambda x: x[0])
            # 处理三星出货日期
            for date in class_.date.date_wap_3:
                if date not in class_.date.date_count_wap_3.keys():
                    class_.date.date_count_wap_3[date] = 1
                else:
                    class_.date.date_count_wap_3[date] += 1
            class_.date.date_countlist_wap_3 += sorted(Tool().dict_to_list(class_.date.date_count_wap_3),
                                                       key=lambda x: x[0])
        for class_ in self.class_list:  # 处理总计数
            # 处理四星出货时间
            for time in class_.time.time_count_all_4.keys():
                if time not in self.time_all_data_4.keys():
                    self.time_all_data_4[time] = class_.time.time_count_all_4[time]
                else:
                    self.time_all_data_4[time] += class_.time.time_count_all_4[time]

            # 处理五星出货时间
            for time in class_.time.time_count_all_5.keys():
                if time not in self.time_all_data_5.keys():
                    self.time_all_data_5[time] = class_.time.time_count_all_5[time]
                else:
                    self.time_all_data_5[time] += class_.time.time_count_all_5[time]

            # 处理三星出货时间
            for time in class_.time.time_count_wap_3.keys():
                if time not in self.time_all_data_3.keys():
                    self.time_all_data_3[time] = class_.time.time_count_wap_3[time]
                else:
                    self.time_all_data_3[time] += class_.time.time_count_wap_3[time]

            # 处理四星出货日期
            for date in class_.date.date_count_all_4.keys():
                if date not in self.date_all_data.keys():
                    self.date_all_data[date] = class_.date.date_count_all_4[date]
                else:
                    self.date_all_data[date] += class_.date.date_count_all_4[date]

            # 处理五星出货日期
            for date in class_.date.date_count_all_5.keys():
                if date not in self.date_all_data.keys():
                    self.date_all_data[date] = class_.date.date_count_all_5[date]
                else:
                    self.date_all_data[date] += class_.date.date_count_all_5[date]
            # 处理三星出货日期
            for date in class_.date.date_count_wap_3.keys():
                if date not in self.date_all_data.keys():
                    self.date_all_data[date] = class_.date.date_count_wap_3[date]
                else:
                    self.date_all_data[date] += class_.date.date_count_wap_3[date]

        self.date_all_datalist += sorted(Tool().dict_to_list(self.date_all_data), key=lambda x: x[0])
        self.time_all_datalist_3 += sorted(Tool().dict_to_list(self.time_all_data_3), key=lambda x: x[0])
        self.time_all_datalist_4 += sorted(Tool().dict_to_list(self.time_all_data_4), key=lambda x: x[0])
        self.time_all_datalist_5 += sorted(Tool().dict_to_list(self.time_all_data_5), key=lambda x: x[0])

    def maindata_process(self):  # 数据分类
        for class_ in self.class_list:
            _date = class_.date
            _time = class_.time
            for sth in class_.total:
                if sth['rank_type'] == '3':
                    class_.wap_3.append(sth)
                    _date.date_wap_3.append(sth['time'].split(' ')[0])
                    _time.time_wap_3.append(sth['time'].split(' ')[1].split(':')[0])
                elif sth['rank_type'] == '4':
                    if sth['item_type'] == '角色':
                        class_.char_4.append(sth)
                        _date.date_char_4.append(sth['time'].split(' ')[0])
                        _time.time_char_4.append(sth['time'].split(' ')[1].split(':')[0])
                    elif sth['item_type'] == '武器':
                        class_.wap_4.append(sth)
                        _date.date_wap_4.append(sth['time'].split(' ')[0])
                        _time.time_wap_4.append(sth['time'].split(' ')[1].split(':')[0])
                elif sth['rank_type'] == '5':
                    if sth['item_type'] == '角色':
                        class_.char_5.append(sth)
                        _date.date_char_5.append(sth['time'].split(' ')[0])
                        _time.time_char_5.append(sth['time'].split(' ')[1].split(':')[0])
                    elif sth['item_type'] == '武器':
                        class_.wap_5.append(sth)
                        _date.date_wap_5.append(sth['time'].split(' ')[0])
                        _time.time_wap_5.append(sth['time'].split(' ')[1].split(':')[0])

    def merge_data(self, read_data):  # 新旧数据混合
        _charactivity = self.charactivity
        _wapactivity = self.wapactivity
        _permanent = self.permanent
        _novice = self.novice
        for sth in read_data:
            if sth not in _charactivity.total and (sth['gacha_type'] == '301' or sth['gacha_type'] == '400'):
                _charactivity.total.append(sth)
            if sth not in _wapactivity.total and sth['gacha_type'] == '302':
                _wapactivity.total.append(sth)
            if sth not in _permanent.total and sth['gacha_type'] == '200':
                _permanent.total.append(sth)
            if sth not in _novice.total and sth['gacha_type'] == '100':
                _novice.total.append(sth)
        self.ensure_count_process()  # 混合完成直接添加保底计数

    def request_data_processor(self, src_data, gacha_type):  # 数据初步分类
        if src_data != []:
            self.ALL_DATA += src_data
        if src_data == []:
            {}  # 跳过空列表
        elif gacha_type == 400 or gacha_type == 301:  # 角色活动祈愿
            self.charactivity.total += (src_data)
            # print(self.charactivity().total)
            # self.charactivity().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 302:  # 武器活动祈愿
            self.wapactivity.total += (src_data)
            # self.wapactivity().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 200:  # 常驻祈愿
            self.permanent.total += (src_data)
            # self.permanent().total.sort(key=operator.itemgetter('id'),reverse = True)
        elif gacha_type == 100:  # 新手祈愿
            self.novice.total += (src_data)
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

    def getSrcdata(self, gacha_type, server):
        global URL
        page, endid = 1, 0
        src_url = URL[server]
        while True:
            url, request_data = Log().transURL(src_url, gacha_type, page, endid)

            response_list = Tool().get(url, request_data)
            if response_list == []: break  # 无数据提前跳出
            if response_list == 'visit too frequently':
                continue  # 防止请求频繁
            else:
                for sth in response_list:
                    sth['id'] = int(sth['id'])
                self.request_data_processor(response_list, gacha_type)  # 送至处理函数
            if len(response_list) != 20: break  # 最后一页跳出
            # 处理结束ID
            endid = response_list[len(response_list) - 1]['id']

            # 处理页数

            if (gacha_type == 200):  # 常驻祈愿
                print("获取 " + server + " 常驻祈愿 " + str(page) + ' 页')

            elif (gacha_type == 100):  # 新手祈愿
                print("获取 " + server + " 新手祈愿 " + str(page) + ' 页')

            elif (gacha_type == 301 or gacha_type == 400):  # 角色活动祈愿
                print("获取 " + server + " 角色活动祈愿 " + str(page) + ' 页')

            elif (gacha_type == 302):  # 武器活动祈愿
                print("获取 " + server + " 武器活动祈愿 " + str(page) + ' 页')

            page += 1


class Tool():  # 工具类函数
    def EXIT(self):  # 退出
        os.system('taskkill /pid ' + str(os.getpid()) + ' /f')

    def SAVE(self, srcData):

        uid_src = srcData[0]['uid']
        uid_file = []
        for file in glob.glob("*.txt"):
            if "藏弓待用" in file:
                uid_file.append(eval(open(self_path + '/' + file, 'r', encoding='utf-8').readline())[0]['uid'])
        if uid_src in uid_file:
            data_file = eval(open(self_path + '/' + '藏弓待用' + uid_src + '.txt', 'r', encoding='utf-8').readline())
            for sth in srcData:
                if sth not in data_file:
                    data_file.append(sth)
            open(self_path + '/' + '藏弓待用' + uid_src + '.txt', "w+", encoding="utf-8").writelines(str(data_file))
        else:
            open(self_path + '/' + '藏弓待用' + uid_src + '.txt', "w+", encoding="utf-8").writelines(str(srcData))

    def READ(self, uid, path=os.getcwd()):
        return eval(open(path + '/' + '藏弓待用' + uid + '.txt', "r", encoding="utf-8").readline())

    def dict_to_list(self, dict={}):  # 字典转列表
        dictlist = []
        for keys, value in dict.items():
            temp = [keys, value]
            dictlist.append(temp)
        # print(dictlist)
        return dictlist

    def get(self, src_url, src_data):  # get数据
        src_data['timestamp'] = int(t.time())  # 使用实时时间
        response = requests.get(src_url, src_data)
        # print(response.text)
        if 'visit too frequently' in response.text:
            t.sleep(0.5)  # 防止请求频繁
            return 'visit too frequently'


        elif 'null' in response.text:
            raise "URL ERROR !"

        return eval(response.text)['data']['list']


class Log():
    def transURL(self, url_forfirst, gacha_type, page, end_id):
        authkey_ver = int(url_forfirst[url_forfirst.index('authkey_ver=') + 12])
        sign_type = int(url_forfirst[url_forfirst.index('sign_type=') + 10])
        auth_appid = url_forfirst[url_forfirst.index('auth_appid=') + 11:url_forfirst.index('&init_type')]
        init_type = int(url_forfirst[url_forfirst.index('init_type=') + 10:url_forfirst.index('&gacha_id')])
        gacha_id = url_forfirst[url_forfirst.index('gacha_id=') + 9:url_forfirst.index('&timestamp')]
        timestamp = int(url_forfirst[url_forfirst.index('timestamp=') + 10:url_forfirst.index('&lang')])
        device_type = url_forfirst[url_forfirst.index('device_type=') + 12:url_forfirst.index('&ext')]
        game_version = url_forfirst[url_forfirst.index('game_version=') + 13:url_forfirst.index('&plat_type')]
        plat_type = url_forfirst[url_forfirst.index('plat_type=') + 10:url_forfirst.index('&region')]
        region = url_forfirst[url_forfirst.index('region=') + 7:url_forfirst.index('&authkey')]
        authkey = url_forfirst[url_forfirst.index('authkey=') + 8:url_forfirst.index('&game_biz')]
        game_biz = url_forfirst[url_forfirst.index('game_biz=') + 9:url_forfirst.index('#/log')]
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
            'authkey': urllib.parse.unquote(authkey),  #
            'game_biz': game_biz,
            'gacha_type': gacha_type,
            'page': page,
            'size': 20,
            'end_id': end_id
        }
        if 'cn' not in region:
            url = '''https://hk4e-api-os.hoyoverse.com/event/gacha_info/api/getGachaLog'''
        else:
            url = '''https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'''
        return url, data

    def getURL(self):
        global URL
        print('\nChecking...')
        if os.path.exists('url_CN.txt'):
            _url = open('url_CN.txt', 'r', encoding='UTF-8').read()

            if not self.checkURL(_url):
                self.updateURL(0)
            else:
                URL['国服'] = _url
                print("\nCN")
        else:
            self.updateURL(0)
        if os.path.exists('url_OS.txt'):
            _url = open('url_OS.txt', 'r', encoding='UTF-8').read()

            if not self.checkURL(_url):
                self.updateURL(1)
            else:
                URL['国际服'] = _url
                print("\nOS")
        else:
            self.updateURL(1)
        if URL['国服'] == '' and URL['国际服'] == '':
            print('\nNone of URL is available !')
            Tool().EXIT()
        return 1

    def updateURL(self, type):
        global URL

        if os.path.exists(log_path_in) and (type == 0 or type == 2):  # 获取国服链接
            print("\nUpdating cn URL ...")
            log = open(log_path_in, 'r', encoding='UTF-8').read()
            start = log.rfind('https://webstatic.mihoyo.com/hk4e/event/')
            end = log.rfind('#/log') + 5
            url_in = str(log[start:end])
            open('url_CN.txt', 'w+', encoding='UTF-8').write(url_in)
            URL['国服'] = url_in
            # print("检查国服链接")
            if url_in == '':
                print("\nCN URL Is Empty")
            else:
                if not self.checkURL(url_in):
                    print("\n国服链接失效\n请登录 原神->祈愿->历史记录 刷新链接后重试")
                    URL['国服'] = ''

                else:
                    print("\nCN")
        if os.path.exists(log_path_out) and (type == 1 or type == 2):  # 获取外服链接
            print("\nUpdating os URL ...")
            log = open(log_path_out, 'r', encoding='UTF-8').read()
            start = log.rfind('https://webstatic-sea.hoyoverse.com/genshin/event/')
            end = log.rfind('#/log') + 5
            url_out = str(log[start:end])
            open('url_OS.txt', 'w+', encoding='UTF-8').write(url_out)
            URL["国际服"] = url_out
            # print("检查国际服链接")
            if url_out == '':
                print("\nOS URL Is Empty")
            else:
                if not self.checkURL(url_out):
                    print("\n国际服链接失效\n请登录 原神->祈愿->历史记录 刷新链接后重试")
                    URL['国际服'] = ''
                else:
                    print("\nOS")

    def checkURL(self, url):
        try:
            _url, _data = self.transURL(url, 301, 1, 0)
            Tool().get(_url, _data)  # 获取一次以校验链接
            return 1
        except Exception as e:
            # print(e)
            return 0


class charts():  # 图表类
    def __init__(self, sever_class):
        self.sever_class = sever_class

    def make_pie(self, data_class):  # 构造饼图对象，传入数据类
        wap3, char4, wap4, char5, wap5 = self.sever_class.make_detail(data_class)
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
        for day in self.sever_class.date_all_datalist:
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
                    title_opts=pyecharts.options.TitleOpts(pos_left="left", title="祈愿日历"),
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
                    title_opts=pyecharts.options.TitleOpts(pos_left="left", title="祈愿日历"),
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

        data_3 = self.sever_class.time_all_datalist_3
        data_4 = self.sever_class.time_all_datalist_4
        data_5 = self.sever_class.time_all_datalist_5
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
        page = pyecharts.charts.Page(page_title='山泽麟迹' + str(self.sever_class.ALL_DATA[0]['uid']),
                                     layout=pyecharts.charts.Page.DraggablePageLayout)

        if self.sever_class.charactivity.total != []:
            pie_char = self.make_pie(self.sever_class.charactivity)
            page.add(pie_char)
        else:
            pie_char = 0
            print('\n' + str(self.sever_class.ALL_DATA[0]['uid']) + "角色活动祈愿为空")

        if self.sever_class.wapactivity.total != []:
            pie_wap = self.make_pie(self.sever_class.wapactivity)
            page.add(pie_wap)
        else:
            pie_wap = 0
            print('\n' + str(self.sever_class.ALL_DATA[0]['uid']) + "武器活动祈愿为空")

        if self.sever_class.permanent.total != []:
            pie_per = self.make_pie(self.sever_class.permanent)
            page.add(pie_per)

        else:
            pie_per = 0
            print('\n' + str(self.sever_class.ALL_DATA[0]['uid']) + "常驻祈愿为空")

        if self.sever_class.novice.total != []:
            pie_nov = self.make_pie(self.sever_class.novice)
            page.add(pie_nov)
        else:
            pie_nov = 0
            print('\n' + str(self.sever_class.ALL_DATA[0]['uid']) + "新手祈愿为空")

        scatter = self.make_scatter()
        page.add(scatter)
        calendar2021, calendar2022 = self.make_calendar()

        # page.add(pie1,pie2,pie3).render('TEST.html')#添加图表,不含日历图
        if calendar2021 != 0:
            page.add(calendar2021)
        else:
            print(str(self.sever_class.ALL_DATA[0]['uid']) + " 2021 data not found")
        if calendar2022 != 0:
            page.add(calendar2022)
        else:
            print(str(self.sever_class.ALL_DATA[0]['uid']) + " 2022 data not found")
        page.render(self_path + '/' + 'TEST' + str(self.sever_class.ALL_DATA[0]['uid']) + '.html')
        page.save_resize_html(self_path + '/' + 'TEST' + str(self.sever_class.ALL_DATA[0]['uid']) + '.html',
                              cfg_file=self_path + '/chart_config.json',
                              dest=self_path + '/' + '山泽麟迹' + str(self.sever_class.ALL_DATA[0]['uid']) + '.html')
        os.remove(self_path + '/' + 'TEST' + str(self.sever_class.ALL_DATA[0]['uid']) + '.html')
        # 需要改变图表布局则屏蔽这两行，在测试网页里保存配置(*.json)，或者直接修改


def getData(server):
    global data_cn, data_os
    if server == '国服':
        _data = data_cn
    elif server == '国际服':
        _data = data_os
    else:
        raise ValueError("Unexpected server")
    thread_301 = threading.Thread(target=_data.getSrcdata, args=(301, server,))
    thread_302 = threading.Thread(target=_data.getSrcdata, args=(302, server,))
    thread_200 = threading.Thread(target=_data.getSrcdata, args=(200, server,))
    thread_100 = threading.Thread(target=_data.getSrcdata, args=(100, server,))
    thread_301.start()
    thread_302.start()
    thread_200.start()
    thread_100.start()


def processData(server):
    global data_cn, data_os
    if server == '国服':
        _data = data_cn
    elif server == '国际服':
        _data = data_os
    else:
        raise ValueError("Unexpected server")
    Tool().SAVE(_data.ALL_DATA)

    _data.merge_data(Tool().READ(_data.ALL_DATA[0]['uid']))

    _data.maindata_process()

    _data.datetimedata_process()


def drawCharts(server):
    global data_cn, data_os
    if server == '国服':
        _data = data_cn
    elif server == '国际服':
        _data = data_os
    else:
        raise ValueError("Unexpected server")
    _charts = charts(_data)

    _charts.draw_charts()
    webbrowser.open(self_path + '/' + '山泽麟迹' + str(_data.ALL_DATA[0]['uid']) + '.html')


def main():
    global URL
    Initialization()

    Log().getURL()
    print("\nGetting data from miHoYo API ...\n")
    if URL['国服'] != '':
        getData('国服')
    if URL['国际服'] != '':
        getData('国际服')
    while True:
        # t.sleep(0.5)
        if len(threading.enumerate()) == 1: break
    print("\nProcessing data and drawing ...")
    if URL['国服'] != '':
        processData('国服')
    if URL['国际服'] != '':
        processData('国际服')

    if URL['国服'] != '':
        drawCharts('国服')
    if URL['国际服'] != '':
        drawCharts('国际服')
    print("\nSuccess ! ")
    print('\nExit...')
    os.remove('cacert.pem')
    t.sleep(3)
    Tool().EXIT()


l_path = ''
self_path = ''
log_path_in = ''
log_path_out = ''
URL = {'国服': '', '国际服': ''}
data_cn = data()
data_os = data()
try:
    main()
except Exception as e:
    print('\nUnexcept Error : \n')
    print(e)
    print("\n请联系开发者\n")
    print('\nExit in 15 sec')
    t.sleep(15)
    Tool().EXIT()
