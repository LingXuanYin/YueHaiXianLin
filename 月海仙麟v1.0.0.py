import requests
import os
import re
import time
import sys
import win32api
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), '''cacert.pem''')
file_web = resource_path(os.path.join("res", "数据展示.html"))
file_dem = resource_path(os.path.join("res", "cacert.pem"))
open("cacert.pem",'w').close()
open("cacert.pem",'r+').write( open(file_dem,'r+').read())

#获取日志
url_query='''https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?'''



#常驻  200
#新手  100 
#角色活动  301
#武器活动  302
def get_data(url_forfirst,gacha_type,page,end_id):
    try:
        authkey_ver=int(url_forfirst[url_forfirst.index('authkey_ver=')+12])
    except:
        print("authkey_ver不可用")
        authkey_ver="1"
    try:
        sign_type=int(url_forfirst[url_forfirst.index('sign_type=')+10])
    except:
        print("sign_type不可用")
        sign_type="2"
    try:
        auth_appid=url_forfirst[url_forfirst.index('auth_appid=')+11:url_forfirst.index('&init_type')]
    except:
        print("auth_appid不可用")
        auth_appid="webview_gacha"
    try:    
        init_type=int(url_forfirst[url_forfirst.index('init_type=')+10:url_forfirst.index('&gacha_id')])
    except:
        print("init_type不可用")
        init_type="301"
    try:    
        gacha_id=url_forfirst[url_forfirst.index('gacha_id=')+9:url_forfirst.index('&timestamp')]
    except:
        raise Exception("gacha_id不可用")
    try:    
        timestamp=int(url_forfirst[url_forfirst.index('timestamp=')+10:url_forfirst.index('&lang')])
    except:
        print("timestamp不可用")
        timestamp=int(time.time())
    try:
        device_type=url_forfirst[url_forfirst.index('device_type=')+12:url_forfirst.index('&ext')]
    except:
        print("device_type不可用")
        device_type="pc"
    try:
        game_version=url_forfirst[url_forfirst.index('game_version=')+13:url_forfirst.index('&plat_type')]
    except:
        raise Exception("game_version不可用")
    try:
        plat_type=url_forfirst[url_forfirst.index('plat_type=')+10:url_forfirst.index('&region')]
    except:
        print("plat_type不可用")
        plat_type="pc"
    try:
        region=url_forfirst[url_forfirst.index('region=')+7:url_forfirst.index('&authkey')]
    except:
        print("authkey_ver不可用")
        region="cn_gf01"
    try:
        authkey=url_forfirst[url_forfirst.index('authkey=')+8:url_forfirst.index('&game_biz')]
    except:
        raise Exception("authkey_ver不可用")
    try:
        game_biz=url_forfirst[url_forfirst.index('game_biz=')+9:url_forfirst.index('#/log')]
    except:
        print("game_biz不可用")
        game_biz="hk4e_cn"

    data={
        'authkey_ver':authkey_ver,
        'sign_type':sign_type,
        'auth_appid':auth_appid,
        'init_type':init_type,
        'gacha_id':gacha_id,
        'timestamp':timestamp,
        'lang':'zh-cn',
        'device_type':device_type,
        'game_version':game_version,
        'plat_type':plat_type,
        'region':region,
        'authkey':authkey,
        'game_biz':game_biz,
        'gacha_type':gacha_type,
        'page':page,
        'size':20,
        'end_id':end_id
    }

    return data



def get_url():
    log_path='''.\output_log.txt'''
    log_file=open(log_path,'r+',encoding='UTF-8')
    file_buf=log_file.read()
    start=file_buf.index('''https://webstatic.mihoyo.com/hk4e/event/''')
    end=file_buf.index('''#/log''')+5
    url_forfirst=file_buf[start:end]

    return url_forfirst

    
def get_log():
    try:
        log_path=os.getenv("APPDATA")
    except:
        log_path=input()("获取日志目录失败，请手动输入\n 示例:C:\\Users\\Username\\AppData\\LocalLow\\")
        
    log_path=os.path.join(log_path, "..\\")+"LocalLow\\miHoYo\\原神\\output_log.txt"
    try:
        if(not os.path.exists(log_path) or os.stat(log_path).st_mtime>time.time()+60*60*24 or open(log_path,'r+',encoding='UTF-8').read()==""):
            raise Exception("链接已过期或不存在，请打开原神查询界面刷新日志后重试")
    except:
        raise Exception("链接已过期或不存在，请打开原神查询界面刷新日志后重试")
    #判断日志文件是否存在或为空或过期
    if(not os.path.exists('''.\output_log.txt''') or os.stat('''.\output_log.txt''').st_mtime>time.time()+60*60*24 or open('''.\output_log.txt''','r+',encoding='UTF-8').read()==""):
        open('''.\output_log.txt''','w+',encoding='UTF-8').write( open(log_path,'r+',encoding='UTF-8').read())



def get_result(gacha_type):
    global url_query

    get_log()
    try:

        url_forfirst=get_url()

        data= get_data(url_forfirst, 200, 1, 0)  
        url_buf=url_query
        url_buf=url_buf+'authkey_ver' +'='+str(data['authkey_ver'])
        del data['authkey_ver']
        for key in data:
            url_buf=url_buf+'''&'''+key+'=' +str(data[key])
        response= requests.get(url_buf)
        result_dic=eval(response.text)
    except:
        os.remove('output_log.txt')
        get_log()
        try:

            url_forfirst=get_url()
            data= get_data(url_forfirst, 200, 1, 0)    
            url_buf=url_query
            url_buf=url_buf+'authkey_ver' +'='+str(data['authkey_ver'])
            del data['authkey_ver']
            for key in data:
                url_buf=url_buf+'''&'''+key+'=' +str(data[key])
            response= requests.get(url_buf)
            result_dic=eval(response.text)
        except:
            os.remove('output_log.txt')

            print("日志文件损坏\n请打开原神查询界面刷新日志")
            time.sleep(5)
            raise Exception("日志文件损坏\n请打开原神查询界面刷新日志")
    #gacha_type=int(url_forfirst[url_forfirst.index('init_type=')+10:url_forfirst.index('''&gacha_id''')])
    result_dic={}
    result_list={}
    page=1
    end_id=0
    if(gacha_type==200):
        pri_text="常驻祈愿"
    elif(gacha_type==100):
        pri_text="新手祈愿"
    elif(gacha_type==301):
        pri_text="角色活动祈愿"
    elif(gacha_type==302):
        pri_text="武器活动祈愿"
    while(True):
        print("正在截取 "+pri_text+" 第 "+str(page)+" 页 ")
        data=get_data(url_forfirst, gacha_type, page, end_id)
        if data=='':
            print ("链接已过期或不存在，请打开原神查询界面刷新日志后重试,或删除文件夹下的output_log.txt再试")
            os.remove("output_log.txt")
            time.sleep(5)
            raise Exception("链接已过期或不存在，请打开原神查询界面刷新日志后重试,或删除文件夹下的output_log.txt再试")
        url_buf=url_query
        url_buf=url_buf+'authkey_ver' +'='+str(data['authkey_ver'])
        del data['authkey_ver']
        for key in data:
            url_buf=url_buf+'''&'''+key+'=' +str(data[key])
        response= requests.get(url_buf)
        try:
            result_dic=eval(response.text)

        except:
            if(response.text.index('visit too frequently')):
                time.sleep(0.5)
                response= requests.get(url_buf)
                result_dic=eval(response.text)

            else:
                open('''.\output_log.txt''','w',encoding='UTF-8')
                raise Exception("链接已重置")

        result_list["page"+str(page)]= result_dic['data']['list']

        
        if(len(result_list["page"+str(page)])!=20):
            break

        end_id=result_list["page"+str(page)][len(result_list["page"+str(page)])-1]['id']
        page=page+1

    return result_list

ch1_totalname=[]
ch1_totaltime=[]
ch2_totalname=[]
ch2_totaltime=[]
ch3_totalname=[]
ch3_totaltime=[]
ch4_totalname=[]
ch4_totaltime=[]


ch1_charname_4=[]
ch1_charname_5=[]
ch1_wapname_4=[]
ch1_wapname_5=[]
ch1_charcode_4=[]
ch1_charcode_5=[]
ch1_wapcode_4=[]
ch1_wapcode_5=[]
ch1_chartime_4=[]
ch1_chartime_5=[]
ch1_waptime_4=[]
ch1_waptime_5=[]
#
ch2_charname_4=[]
ch2_charname_5=[]
ch2_wapname_4=[]
ch2_wapname_5=[]
ch2_charcode_4=[]
ch2_charcode_5=[]
ch2_wapcode_4=[]
ch2_wapcode_5=[]
ch2_chartime_4=[]
ch2_chartime_5=[]
ch2_waptime_4=[]
ch2_waptime_5=[]
#
ch3_charname_4=[]
ch3_charname_5=[]
ch3_wapname_4=[]
ch3_wapname_5=[]
ch3_charcode_4=[]
ch3_charcode_5=[]
ch3_wapcode_4=[]
ch3_wapcode_5=[]
ch3_chartime_4=[]
ch3_chartime_5=[]
ch3_waptime_4=[]
ch3_waptime_5=[]
#
ch4_charname_4=[]
ch4_charname_5=[]
ch4_wapname_4=[]
ch4_wapname_5=[]
ch4_charcode_4=[]
ch4_charcode_5=[]
ch4_wapcode_4=[]
ch4_wapcode_5=[]
ch4_chartime_4=[]
ch4_chartime_5=[]
ch4_waptime_4=[]
ch4_waptime_5=[]
#
ch1_totaltype=[]
ch2_totaltype=[]
ch3_totaltype=[]
ch4_totaltype=[]


ch1_result_list= get_result(200)
ch2_result_list=get_result(100)
ch3_result_list=get_result(301)
ch4_result_list=get_result(302)

i=0
flag=0
for item in ch1_result_list:
    list_buf=ch1_result_list[item]
    for value in list_buf:

        ch1_totaltype.append(list_buf[i]['item_type'])
        ch1_totalname.append(list_buf[i]['name'])
        ch1_totaltime.append(list_buf[i]['time'])
        if(list_buf[i]['rank_type'] == '5'):
            if (list_buf[i]['item_type'] == '武器'):
                ch1_wapcode_5.append(str(flag))
                ch1_wapname_5.append(list_buf[i]['name'] )
                ch1_waptime_5.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch1_charcode_5.append(str(flag))
                ch1_charname_5.append(list_buf[i]['name'] )
                ch1_chartime_5.append( list_buf[i]['time'])
        elif(list_buf[i]['rank_type'] == '4'):
            if (list_buf[i]['item_type'] == '武器'):
                ch1_wapcode_4.append(str(flag))
                ch1_wapname_4.append(list_buf[i]['name'] )
                ch1_waptime_4.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch1_charcode_4.append(str(flag))
                ch1_charname_4.append(list_buf[i]['name'] )
                ch1_chartime_4.append( list_buf[i]['time'])

        print("处理常驻祈愿第 "+str(flag)+" 条数据")
        i=i+1
        flag=flag+1
    i=0


i=0
flag=0
for item in ch2_result_list:
    list_buf=ch2_result_list[item]
    for value in list_buf:
        ch2_totaltype.append(list_buf[i]['item_type'])
        ch2_totalname.append(list_buf[i]['name'])
        ch2_totaltime.append(list_buf[i]['time'])
        if(list_buf[i]['rank_type'] == '5'):
            if (list_buf[i]['item_type'] == '武器'):
                ch2_wapcode_5.append(str(flag))
                ch2_wapname_5.append(list_buf[i]['name'] )
                ch2_waptime_5.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch2_charcode_5.append(str(flag))
                ch2_charname_5.append(list_buf[i]['name'] )
                ch2_chartime_5.append( list_buf[i]['time'])
        elif(list_buf[i]['rank_type'] == '4'):
            if (list_buf[i]['item_type'] == '武器'):
                ch2_wapcode_4.append(str(flag))
                ch2_wapname_4.append(list_buf[i]['name'] )
                ch2_waptime_4.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch2_charcode_4.append(str(flag))
                ch2_charname_4.append(list_buf[i]['name'] )
                ch2_chartime_4.append( list_buf[i]['time'])

        print("处理新手祈愿第 "+str(flag)+" 条数据")
        i=i+1
        flag=flag+1
    i=0

i=0
flag=0
for item in ch3_result_list:
    list_buf=ch3_result_list[item]
    for value in list_buf:

        ch3_totaltype.append(list_buf[i]['item_type'])
        ch3_totalname.append(list_buf[i]['name'])
        ch3_totaltime.append(list_buf[i]['time'])
        if(list_buf[i]['rank_type'] == '5'):
            if (list_buf[i]['item_type'] == '武器'):
                ch3_wapcode_5.append(str(flag))
                ch3_wapname_5.append(list_buf[i]['name'] )
                ch3_waptime_5.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch3_charcode_5.append(str(flag))
                ch3_charname_5.append(list_buf[i]['name'] )
                ch3_chartime_5.append( list_buf[i]['time'])
        elif(list_buf[i]['rank_type'] == '4'):
            if (list_buf[i]['item_type'] == '武器'):
                ch3_wapcode_4.append(str(flag))
                ch3_wapname_4.append(list_buf[i]['name'] )
                ch3_waptime_4.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch3_charcode_4.append(str(flag))
                ch3_charname_4.append(list_buf[i]['name'] )
                ch3_chartime_4.append( list_buf[i]['time'])

        print("处理角色活动祈愿第 "+str(flag)+" 条数据")
        i=i+1
        flag=flag+1
    i=0

i=0
flag=0
for item in ch4_result_list:
    list_buf=ch4_result_list[item]
    for value in list_buf:
        ch4_totaltype.append(list_buf[i]['item_type'])
        ch4_totalname.append(list_buf[i]['name'])
        ch4_totaltime.append(list_buf[i]['time'])

        if(list_buf[i]['rank_type'] == '5'):
            if (list_buf[i]['item_type'] == '武器'):
                ch4_wapcode_5.append(str(flag))
                ch4_wapname_5.append(list_buf[i]['name'] )
                ch4_waptime_5.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch4_charcode_5.append(str(flag))
                ch4_charname_5.append(list_buf[i]['name'] )
                ch4_chartime_5.append( list_buf[i]['time'])
        elif(list_buf[i]['rank_type'] == '4'):
            if (list_buf[i]['item_type'] == '武器'):
                ch4_wapcode_4.append(str(flag))
                ch4_wapname_4.append(list_buf[i]['name'] )
                ch4_waptime_4.append( list_buf[i]['time'])
            elif(list_buf[i]['item_type'] == '角色'):
                ch4_charcode_4.append(str(flag))
                ch4_charname_4.append(list_buf[i]['name'] )
                ch4_chartime_4.append( list_buf[i]['time'])

        print("处理武器活动祈愿第 "+str(flag)+" 条数据")
        i=i+1
        flag=flag+1
    i=0



web = open(file_web, "r", encoding="UTF-8")
web_text = web.readlines()
i=25#源码注入起始行
web.close()
date_path='.\\temp'
if(not os.path.exists(date_path)):
    os.mkdir( date_path)
print(ch1_charname_4,file=open(date_path+"\\temp", "w"))
 
web_text[i] = "var 常驻_charname_4=" +  open(date_path+"\\temp").read()


print(ch1_charname_5,file=open(date_path+"\\temp", "w"))


web_text[i+1] = "var 常驻_charname_5=" +  open(date_path+"\\temp").read()

print(ch1_wapname_4,file=open(date_path+"\\temp", "w"))



web_text[i+2] = "var 常驻_wapname_4=" +  open(date_path+"\\temp").read()

print(ch1_wapname_5,file=open(date_path+"\\temp", "w"))



web_text[i+3] = "var 常驻_wapname_5=" + open(date_path+"\\temp").read()

print(ch1_charcode_4,file=open(date_path+"\\temp", "w"))



web_text[i+4] = "var 常驻_charcode_4=" +  open(date_path+"\\temp").read()

print(ch1_charcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 5] = "var 常驻_charcode_5=" +  open(date_path+"\\temp").read()

print(ch1_wapcode_4,file=open(date_path+"\\temp", "w"))


web_text[i + 6] = "var 常驻_wapcode_4=" +  open(date_path+"\\temp").read()

print(ch1_wapcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 7] = "var 常驻_wapcode_5=" +  open(date_path+"\\temp").read()

print(ch1_chartime_4,file=open(date_path+"\\temp", "w"))



web_text[i + 8] = "var 常驻_chartime_4=" +  open(date_path+"\\temp").read()

print(ch1_chartime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 9] = "var 常驻_chartime_5=" +   open(date_path+"\\temp").read()

print(ch1_waptime_4,file=open(date_path+"\\temp", "w"))


web_text[i + 10] = "var 常驻_waptime_4=" +  open(date_path+"\\temp").read()

print(ch1_waptime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 11] = "var 常驻_waptime_5=" +   open(date_path+"\\temp").read()

print(ch1_totalname,file=open(date_path+"\\temp", "w"))


web_text[i + 12] = "var 常驻_totalname=" +   open(date_path+"\\temp").read()

print(ch1_totaltime,file=open(date_path+"\\temp", "w"))


web_text[i + 14] = "var 常驻_totaltime=" +  open(date_path+"\\temp").read()


print(ch2_charname_4,file=open(date_path+"\\temp", "w"))



web_text[i+16] = "var 新手_charname_4=" +  open(date_path+"\\temp").read()
print(ch2_charname_5,file=open(date_path+"\\temp", "w"))



web_text[i+17] = "var 新手_charname_5=" +  open(date_path+"\\temp").read()
print(ch2_wapname_4,file=open(date_path+"\\temp", "w"))



web_text[i+18] = "var 新手_wapname_4=" +  open(date_path+"\\temp").read()
print(ch2_wapname_5,file=open(date_path+"\\temp", "w"))



web_text[i+19] = "var 新手_wapname_5=" + open(date_path+"\\temp").read()
print(ch2_charcode_4,file=open(date_path+"\\temp", "w"))



web_text[i+20] = "var 新手_charcode_4=" +  open(date_path+"\\temp").read()
print(ch2_charcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 21] = "var 新手_charcode_5=" +  open(date_path+"\\temp").read()
print(ch2_wapcode_4,file=open(date_path+"\\temp", "w"))


web_text[i + 22] = "var 新手_wapcode_4=" +  open(date_path+"\\temp").read()
print(ch2_wapcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 23] = "var 新手_wapcode_5=" +  open(date_path+"\\temp").read()
print(ch2_chartime_4,file=open(date_path+"\\temp", "w"))



web_text[i + 24] = "var 新手_chartime_4=" +  open(date_path+"\\temp").read()
print(ch2_chartime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 25] = "var 新手_chartime_5=" +   open(date_path+"\\temp").read()
print(ch2_waptime_4,file=open(date_path+"\\temp", "w"))


web_text[i + 26] = "var 新手_waptime_4=" +  open(date_path+"\\temp").read()
print(ch2_waptime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 27] = "var 新手_waptime_5=" +   open(date_path+"\\temp").read()
print(ch2_totalname,file=open(date_path+"\\temp", "w"))


web_text[i + 28] = "var 新手_totalname=" +   open(date_path+"\\temp").read()
print(ch2_totaltime,file=open(date_path+"\\temp", "w"))


web_text[i + 29] = "var 新手_totaltime=" +  open(date_path+"\\temp").read()
print(ch3_charname_4,file=open(date_path+"\\temp", "w"))



web_text[i+31] = "var 角色_charname_4=" +  open(date_path+"\\temp").read()
print(ch3_charname_5,file=open(date_path+"\\temp", "w"))



web_text[i+32] = "var 角色_charname_5=" +  open(date_path+"\\temp").read()
print(ch3_wapname_4,file=open(date_path+"\\temp", "w"))



web_text[i+33] = "var 角色_wapname_4=" +  open(date_path+"\\temp").read()
print(ch3_wapname_5,file=open(date_path+"\\temp", "w"))



web_text[i+34] = "var 角色_wapname_5=" + open(date_path+"\\temp").read()
print(ch3_charcode_4,file=open(date_path+"\\temp", "w"))



web_text[i+35] = "var 角色_charcode_4=" +  open(date_path+"\\temp").read()
print(ch3_charcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 36] = "var 角色_charcode_5=" +  open(date_path+"\\temp").read()
print(ch3_wapcode_4,file=open(date_path+"\\temp", "w"))


web_text[i + 37] = "var 角色_wapcode_4=" +  open(date_path+"\\temp").read()
print(ch3_wapcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 38] = "var 角色_wapcode_5=" +  open(date_path+"\\temp").read()
print(ch3_chartime_4,file=open(date_path+"\\temp", "w"))



web_text[i + 39] = "var 角色_chartime_4=" +  open(date_path+"\\temp").read()
print(ch3_chartime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 40] = "var 角色_chartime_5=" +   open(date_path+"\\temp").read()
print(ch3_waptime_4,file=open(date_path+"\\temp", "w"))


web_text[i + 41] = "var 角色_waptime_4=" +  open(date_path+"\\temp").read()
print(ch3_waptime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 42] = "var 角色_waptime_5=" +   open(date_path+"\\temp").read()
print(ch3_totalname,file=open(date_path+"\\temp", "w"))


web_text[i + 43] = "var 角色_totalname=" +   open(date_path+"\\temp").read()
print(ch3_totaltime,file=open(date_path+"\\temp", "w"))


web_text[i + 44] = "var 角色_totaltime=" +  open(date_path+"\\temp").read()
print(ch4_charname_4,file=open(date_path+"\\temp", "w"))




web_text[i+46] = "var 武器_charname_4=" +  open(date_path+"\\temp").read()
print(ch4_charname_5,file=open(date_path+"\\temp", "w"))



web_text[i+47] = "var 武器_charname_5=" +  open(date_path+"\\temp").read()
print(ch4_wapname_4,file=open(date_path+"\\temp", "w"))



web_text[i+48] = "var 武器_wapname_4=" +  open(date_path+"\\temp").read()
print(ch4_wapname_5,file=open(date_path+"\\temp", "w"))



web_text[i+49] = "var 武器_wapname_5=" + open(date_path+"\\temp").read()
print(ch4_charcode_4,file=open(date_path+"\\temp", "w"))



web_text[i+50] = "var 武器_charcode_4=" +  open(date_path+"\\temp").read()
print(ch4_charcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 51] = "var 武器_charcode_5=" +  open(date_path+"\\temp").read()
print(ch4_wapcode_4,file=open(date_path+"\\temp", "w"))


web_text[i + 52] = "var 武器_wapcode_4=" +  open(date_path+"\\temp").read()
print(ch4_wapcode_5,file=open(date_path+"\\temp", "w"))


web_text[i + 53] = "var 武器_wapcode_5=" +  open(date_path+"\\temp").read()
print(ch4_chartime_4,file=open(date_path+"\\temp", "w"))



web_text[i + 54] = "var 武器_chartime_4=" +  open(date_path+"\\temp").read()
print(ch4_chartime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 55] = "var 武器_chartime_5=" +   open(date_path+"\\temp").read()
print(ch4_waptime_4,file=open(date_path+"\\temp", "w"))


web_text[i + 56] = "var 武器_waptime_4=" +  open(date_path+"\\temp").read()
print(ch4_waptime_5,file=open(date_path+"\\temp", "w"))


web_text[i + 57] = "var 武器_waptime_5=" +   open(date_path+"\\temp").read()
print(ch4_totalname,file=open(date_path+"\\temp", "w"))


web_text[i + 58] = "var 武器_totalname=" +   open(date_path+"\\temp").read()
print(ch4_totaltime,file=open(date_path+"\\temp", "w"))


web_text[i + 59] = "var 武器_totaltime=" +  open(date_path+"\\temp").read()

open('数据展示.html', "w", encoding="UTF-8").close()
web=open('数据展示.html', "r+", encoding="UTF-8")
web.writelines(web_text)
web.close()


import webbrowser
webbrowser.open("数据展示.html")
os.removedirs(date_path)
win32api.SetFileAttributes('cacert.pem',win32con.FILE_ATTRIBUTE_HIDDEN)
win32api.SetFileAttributes('output_log.txt',win32con.FILE_ATTRIBUTE_HIDDEN)

#ch1='200'#常驻
#ch2='100'#新手
#ch3='301'#角色活动
#ch4='302'#武器活动



