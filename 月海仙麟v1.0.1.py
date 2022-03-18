import os
import sys
import requests
import random
import pyecharts
import operator
import re
import Save
import glob
import webbrowser
import time
self_path=os.getcwd()
#print(self_path)
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), '''cacert.pem''')
file_json= resource_path(os.path.join("res","chart_config.json"))
file_dem = resource_path(os.path.join("res","cacert.pem"))
open("cacert.pem",'w+').write( open(file_dem,'r+').read())

open("chart_config.json",'w+').write( open(file_json,'r+').read())

###########
if not os.path.exists('chart_config.json'):
    open("chart_config.json",'w+').writelines(open(file_json,'r+',encoding='utf-8').read())

#资源文件


class Log():#日志类
    #复制日志文件到根目录
    def __init__(self):
        {}
    def get_log(self):
        

        if(os.path.exists('./output_log.txt') and os.stat('./output_log.txt').st_mtime<time.time()+60*60*24 and not open('./output_log.txt','r',encoding='UTF-8').read()=="") :
            return 0
        l_path=os.getenv("APPDATA")
        #log_path=input("获取日志目录失败，请手动输入/n 示例:C://Users//Username//AppData//LocalLow//")
        
        log_path=os.path.join(l_path, "../")+"LocalLow/miHoYo/原神/output_log.txt"
        log_last_path=os.path.join(l_path, "../")+"LocalLow/miHoYo/原神/output_log.txt.last"
        if(not os.path.exists(log_path) or os.stat(log_path).st_mtime>time.time()+60*60*24 or open(log_path,'r',encoding='UTF-8').read()=="") :
            if  (not os.path.exists(log_last_path) or os.stat(log_last_path).st_mtime>time.time()+60*60*24 or open(log_last_path,'r',encoding='UTF-8').read()==""):
                
                return "链接已过期或不存在，请打开原神查询界面刷新日志后重试"
            else:
                open('''./output_log.txt''','w+',encoding='UTF-8').write( open(log_last_path,'r',encoding='UTF-8').read())

    #判断日志文件是否存在或为空或过期+
        else:
            open('''./output_log.txt''','w+',encoding='UTF-8').write( open(log_path,'r',encoding='UTF-8').read())

#获取url
    def get_url(self):
        if os.path.exists('''./output_log.txt'''):
            log = open('''./output_log.txt''','r',encoding='UTF-8').read()
    
        start=log.rfind('https://webstatic.mihoyo.com/hk4e/event/')
        end=log.rfind('#/log')+5
        url=str(log[start:end])
        #print(url)
        return url

#处理url，获取认证秘钥等
    def trans_url(self,url_forfirst,gacha_type,page,end_id=0):
        #print(url_forfirst)
        try:
            authkey_ver=int(url_forfirst[url_forfirst.index('authkey_ver=')+12])
        except:
            #print("authkey_ver不可用")
            authkey_ver="1"
        try:
            sign_type=int(url_forfirst[url_forfirst.index('sign_type=')+10])
        except:
            #print("sign_type不可用")
            sign_type="2"
        try:
            auth_appid=url_forfirst[url_forfirst.index('auth_appid=')+11:url_forfirst.index('&init_type')]
        except:
            #print("auth_appid不可用")
            auth_appid="webview_gacha"
        try:    
            init_type=int(url_forfirst[url_forfirst.index('init_type=')+10:url_forfirst.index('&gacha_id')])
        except:
            #print("init_type不可用")
            init_type="301"
        try:    
            gacha_id=url_forfirst[url_forfirst.index('gacha_id=')+9:url_forfirst.index('&timestamp')]
        except: #Exception() as e:
            #open('log.txt', 'a', encoding='utf-8').writelines(str(e))
            raise Exception("gacha_id不可用，请刷新链接")
        try:    
            timestamp=int(url_forfirst[url_forfirst.index('timestamp=')+10:url_forfirst.index('&lang')])
        except:
            #print("timestamp不可用")
            timestamp=int(time.time())#使用实时时间
        try:
            device_type=url_forfirst[url_forfirst.index('device_type=')+12:url_forfirst.index('&ext')]
        except:
            #print("device_type不可用")
            device_type="pc"
        try:
            game_version=url_forfirst[url_forfirst.index('game_version=')+13:url_forfirst.index('&plat_type')]
        except:
            raise Exception("game_version不可用，请刷新链接")
        try:
            plat_type=url_forfirst[url_forfirst.index('plat_type=')+10:url_forfirst.index('&region')]
        except:
            #print("plat_type不可用")
            plat_type="pc"
        try:
            region=url_forfirst[url_forfirst.index('region=')+7:url_forfirst.index('&authkey')]
        except:
            #print("authkey_ver不可用")
            region="cn_gf01"
        try:
            authkey=url_forfirst[url_forfirst.index('authkey=')+8:url_forfirst.index('&game_biz')]
        except:
            raise Exception("authkey_ver不可用，请刷新链接")
        try:
            game_biz=url_forfirst[url_forfirst.index('game_biz=')+9:url_forfirst.index('#/log')]
        except:
            #print("game_biz不可用")
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
        url='''https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?'''
        for key in data:
            
            data['timestamp'] =int(time.time())        

            url=url+'''&'''+key+'=' +str(data[key])
            #print(url)
        #print(url)
        
        return url



class Data():#数据类
    permanent_data=[]#常驻祈愿
    charactivity_data=[]#角色活动祈愿
    wapactivity_data=[]#武器活动祈愿
    novice_data=[]#新手祈愿  
    alldata=[charactivity_data,wapactivity_data,novice_data,permanent_data]
    global self_path

    class permanent():#常驻祈愿
        wap_5=[]
        wap_4=[]
        wap_3=[]
        char_5=[]
        char_4=[]
        ensure_list=[]
        wap5_str=''
        wap4_str=''
        wap3_str=''
        char4_str=''
        char5_str=''
    class charactivity():#角色活动祈愿
        wap_5=[]
        wap_4=[]
        wap_3=[]
        char_5=[]
        char_4=[]
        ensure_list=[]
        wap5_str=''
        wap4_str=''
        wap3_str=''
        char4_str=''
        char5_str=''
    class wapactivity():#武器活动祈愿
        wap_5=[]
        wap_4=[]
        wap_3=[]
        char_5=[]
        char_4=[]
        ensure_list=[]
        wap5_str=''
        wap4_str=''
        wap3_str=''
        char4_str=''
        char5_str=''

    class novice():#新手祈愿
        wap_5=[]
        wap_4=[]
        wap_3=[]
        char_5=[]
        char_4=[]
        ensure_list=[]
        wap5_str=''
        wap4_str=''
        wap3_str=''
        char4_str=''
        char5_str=''
    class_all=[permanent,charactivity,wapactivity,novice]
    
    class prize():#出货数据

        total_extract=0

        class time():#时间数据
            time_char_5=[]#总出货时间
            time_char_4=[]
            time_wap_5=[]
            time_wap_4=[]
            time_all=[]
            time_wap_3=[]

            time_count_char_5={}#时间统计
            time_count_char_4={}
            time_count_wap_5={}
            time_count_wap_4={}
            time_count_all_5={}
            time_count_all_4={}
            time_count_all={}
            time_count_wap_3={}
        class id():

            id_char_5=[]#总出货ID
            id_char_4=[]
            id_wap_5=[]
            id_wap_4=[]

            id_count_char_5={}#ID统计
            id_count_char_4={}
            id_count_wap_5={}
            id_count_wap_4={}
            id_count_all_5={}
            id_count_all_4={}
        class wap_3():
            wap_3_count={}

        class permanent():
            average_pro_4=[0]
            average_cou_4=[0]
            average_pro_5=[0]
            average_cou_5=[0]

        class wapactivity():
            average_pro_4=[0]
            average_cou_4=[0]
            average_pro_5=[0]
            average_cou_5=[0]
            
        class charactivity():
            average_pro_4=[0]
            average_cou_4=[0]
            average_pro_5=[0]
            average_cou_5=[0]
        class novice():
            average_pro_4=[0]
            average_cou_4=[0]
            average_pro_5=[0]
            average_cou_5=[0]

    def prize_count(self):#统计出货
        for i in range(24):
            if i <10:
                j='0'+str(i)
            else:
                j=str(i)
            self.prize().time().time_count_char_5[j]=0
            self.prize().time().time_count_char_4[j]=0
            self.prize().time().time_count_wap_5[j]=0
            self.prize().time().time_count_wap_4[j]=0
            self.prize().time().time_count_all_5[j]=0
            self.prize().time().time_count_all_4[j]=0
            self.prize().time().time_count_all[j]=0
            self.prize().time().time_count_wap_3[j]=0
        for i in range(100):
            self.prize().id().id_count_char_5[str(i)]=0
            self.prize().id().id_count_char_4[str(i)]=0
            self.prize().id().id_count_wap_5[str(i)]=0
            self.prize().id().id_count_wap_4[str(i)]=0
            self.prize().id().id_count_all_5[str(i)]=0
            self.prize().id().id_count_all_4[str(i)]=0
#处理时间
        for time in self.prize().time().time_char_5:
            self.prize().time().time_count_char_5[time.split(' ')[1].split(':')[0]]+=1
            self.prize().time().time_count_all_5[time.split(' ')[1].split(':')[0]]+=1

        for time in self.prize().time().time_char_4:
            self.prize().time().time_count_char_4[time.split(' ')[1].split(':')[0]]+=1
            self.prize().time().time_count_all_4[time.split(' ')[1].split(':')[0]]+=1
            
        for time in self.prize().time().time_wap_5:
            self.prize().time().time_count_wap_5[time.split(' ')[1].split(':')[0]]+=1
            self.prize().time().time_count_all_5[time.split(' ')[1].split(':')[0]]+=1
            
        for time in self.prize().time().time_wap_4:
            self.prize().time().time_count_wap_4[time.split(' ')[1].split(':')[0]]+=1
            self.prize().time().time_count_all_4[time.split(' ')[1].split(':')[0]]+=1
        
        for time in self.prize().time().time_wap_3:
            self.prize().time().time_count_wap_3[time.split(' ')[1].split(':')[0]]+=1
        
        for time in self.prize().time().time_all:
            self.prize().time().time_count_all[time.split(' ')[1].split(':')[0]]+=1
        
#处理ID
        for id in self.prize().id().id_char_5:
            self.prize().id().id_count_char_5[id[len(id)-2:len(id)-1]]+=1
            self.prize().id().id_count_all_5[id[len(id)-2:len(id)-1]]+=1

        for id in self.prize().id().id_char_4:
            self.prize().id().id_count_char_4[id[len(id)-2:len(id)-1]]+=1
            self.prize().id().id_count_all_4[id[len(id)-2:len(id)-1]]+=1

        for id in self.prize().id().id_wap_5:
            self.prize().id().id_count_wap_5[id[len(id)-2:len(id)-1]]+=1
            self.prize().id().id_count_all_5[id[len(id)-2:len(id)-1]]+=1

        for id in self.prize().id().id_wap_4:
            self.prize().id().id_count_wap_4[id[len(id)-2:len(id)-1]]+=1
            self.prize().id().id_count_all_4[id[len(id)-2:len(id)-1]]+=1

#处理三星武器
        for clas in Data().class_all:
            for wap3 in clas.wap_3:
                try:
                    self.prize().wap_3().wap_3_count[wap3['name']]+=1
                except KeyError:
                    self.prize().wap_3().wap_3_count[wap3['name']]=1
        
#处理出货计数
            buf_data=clas.char_4+clas.char_5+clas.wap_4+clas.wap_5
            buf_data.sort(key=operator.itemgetter('ensure_count'))
            #print(buf_data)
            count_buf=0
            for sh in range(len(buf_data)):
                #print(sh)
                
                if buf_data[sh]['rank_type']=='5':
                    buf_data[sh]['ensure_count']= buf_data[sh]['ensure_count']-count_buf
                    count_buf+=buf_data[sh]['ensure_count']
                    
                
                '''elif buf_data[sh]['rank_type'] =='4':
                    buf_data[sh]['ensure_count']=buf_data[sh]['ensure_count']-count_buf
                '''#四星是否参与保底计数重置
                
                    
            #print(buf_data)
            clas.ensure_list=buf_data
            #print(clas.ensure_list)
            #print(Data().wapactivity().ensure_list)
#处理概率
        #print(Data().wapactivity().ensure_list)
        self.prize().wapactivity().average_pro_4[0]=int(((len(Data().wapactivity().char_4)+len(Data().wapactivity().wap_4))/len(Data().charactivity_data))*10000)/100
        self.prize().wapactivity().average_pro_5[0]=int(((len(Data().wapactivity().char_5)+len(Data().wapactivity().wap_5))/len(Data().charactivity_data))*10000)/100
        
        ensure_buf_4,ensure_buf_5=0,0
        for sth in Data().wapactivity().ensure_list:
            if sth['rank_type'] =='4':
                ensure_buf_4+=sth['ensure_count']
            else:
                ensure_buf_5+=sth['ensure_count']
            #print(sth)
        '''try:
            self.prize().wapactivity().average_cou_4=int((ensure_buf_4/(len(Data().wapactivity().char_4)+len(Data().wapactivity().wap_4)))*100)/100
            self.prize().wapactivity().average_cou_5=int((ensure_buf_5/(len(Data().wapactivity().char_5)+len(Data().wapactivity().wap_5)))*100)/100
        except ZeroDivisionError:{}'''
        self.prize().wapactivity().average_cou_4[0]=int((ensure_buf_4/(len(Data().wapactivity().char_4)+len(Data().wapactivity().wap_4)))*100)/100
        self.prize().wapactivity().average_cou_5[0]=int((ensure_buf_5/(len(Data().wapactivity().char_5)+len(Data().wapactivity().wap_5)))*100)/100

    #
        self.prize().permanent().average_pro_4[0]=int(((len(Data().permanent().char_4)+len(Data().permanent().wap_4))/len(Data().charactivity_data))*10000)/100
        self.prize().permanent().average_pro_5[0]=int(((len(Data().permanent().char_5)+len(Data().permanent().wap_5))/len(Data().charactivity_data))*10000)/100
        
        ensure_buf_4,ensure_buf_5=0,0
        for sth in Data().permanent().ensure_list:
            if sth['rank_type'] =='4':
                ensure_buf_4+=sth['ensure_count']
            else:
                ensure_buf_5+=sth['ensure_count']
        '''try:
            self.prize().permanent().average_cou_4=int((ensure_buf_4/(len(Data().permanent().char_4)+len(Data().permanent().wap_4)))*100)/100
            self.prize().permanent().average_cou_5=int((ensure_buf_5/(len(Data().permanent().char_5)+len(Data().permanent().wap_5)))*100)/100
        except ZeroDivisionError:{}'''
        self.prize().permanent().average_cou_4[0]=int((ensure_buf_4/(len(Data().permanent().char_4)+len(Data().permanent().wap_4)))*100)/100
        self.prize().permanent().average_cou_5[0]=int((ensure_buf_5/(len(Data().permanent().char_5)+len(Data().permanent().wap_5)))*100)/100
    #
        self.prize().charactivity().average_pro_4[0]=int(((len(Data().charactivity().char_4)+len(Data().charactivity().wap_4))/len(Data().charactivity_data))*10000)/100
        self.prize().charactivity().average_pro_5[0]=int(((len(Data().charactivity().char_5)+len(Data().charactivity().wap_5))/len(Data().charactivity_data))*10000)/100
        
        ensure_buf_4,ensure_buf_5=0,0
        for sth in Data().charactivity().ensure_list:
            if sth['rank_type'] =='4':
                ensure_buf_4+=sth['ensure_count']
                
            else:
                ensure_buf_5+=sth['ensure_count']
        '''try:
            self.prize().charactivity().average_cou_4=int((ensure_buf_4/(len(Data().charactivity().char_4)+len(Data().charactivity().wap_4)))*100)/100
            self.prize().charactivity().average_cou_5=int((ensure_buf_5/(len(Data().charactivity().char_5)+len(Data().charactivity().wap_5)))*100)/100
        except ZeroDivisionError:{}'''
        self.prize().charactivity().average_cou_4[0]=int((ensure_buf_4/(len(Data().charactivity().char_4)+len(Data().charactivity().wap_4)))*100)/100
        self.prize().charactivity().average_cou_5[0]=int((ensure_buf_5/(len(Data().charactivity().char_5)+len(Data().charactivity().wap_5)))*100)/100
       

    #


        self.prize().novice().average_pro_4[0]=int(((len(Data().novice().char_4)+len(Data().novice().wap_4))/len(Data().charactivity_data))*10000)/100
        self.prize().novice().average_pro_5[0]=int(((len(Data().novice().char_5)+len(Data().novice().wap_5))/len(Data().charactivity_data))*10000)/100
        
        ensure_buf_4,ensure_buf_5=0,0
        for sth in Data().novice().ensure_list:
            if sth['rank_type'] =='4':
                ensure_buf_4+=sth['ensure_count']
            else:
                ensure_buf_5+=sth['ensure_count']
        try:
            self.prize().novice().average_cou_4[0]=int((ensure_buf_4/(len(Data().novice().char_4)+len(Data().novice().wap_4)))*100)/100
            self.prize().novice().average_cou_5[0]=int((ensure_buf_5/(len(Data().novice().char_5)+len(Data().novice().wap_5)))*100)/100
        except ZeroDivisionError:{}
    #
        
        self.total_extract=len(self.prize().wap_3().wap_3_count)+len(self.prize().id().id_count_all_4)+len(self.prize().id().id_count_all_5)
        
    def make_pie(self,data_src,title):
        #绘制饼图
        charts_name='chart_'+title#html中图表名称
        wap3=' '
        wap4=' '
        wap5=' '
        char4=' '
        char5=' '
        
        for i in range(len(data_src.wap_3)):
            wap3+=(' '+data_src.wap_3[i]['name']+' ['+str(data_src.wap_3[i]['ensure_count'])+'] ')
            if i%3==0:
                
                wap3+='</br> '
        
        for i in range(len(data_src.wap_4)):
            wap4+=(' '+data_src.wap_4[i]['name']+' ['+str(data_src.wap_4[i]['ensure_count'])+'] ')
            if i%3==0:
                
                wap4+='</br> '
                
        for i in range(len(data_src.wap_5)):
            wap5+=(' '+data_src.wap_5[i]['name']+' ['+str(data_src.wap_5[i]['ensure_count'])+'] ')
            if i%3==0:
                
                wap5+='</br> '
                
        for i in range(len(data_src.char_5)):
            char5+=(' '+data_src.char_5[i]['name']+' ['+str(data_src.char_5[i]['ensure_count'])+'] ')
            if i%3==0:
                
                char5+='</br> '
                
        for i in range(len(data_src.char_4)):
            char4+=(' '+data_src.char_4[i]['name']+' ['+str(data_src.char_4[i]['ensure_count'])+'] ')
            if i%3==0:
                
                char4+='</br> '
        #print(wap5)
        total_count=0
        data_=[['三星',len(data_src.wap_3)],['四星武器',len(data_src.wap_4)],['四星角色',len(data_src.char_4)],['五星武器',len(data_src.wap_5)],['五星角色',len(data_src.char_5)]]
        for i in data_:
            total_count+=i[1]
        
        pie = (
        pyecharts.charts.Pie(init_opts=pyecharts.options.InitOpts( chart_id=title,theme=pyecharts.globals.ThemeType.MACARONS))#设置id和主题
        .add(
            title,
            data_,
            
            tooltip_opts=pyecharts.options.TooltipOpts
                (
                border_color='red',
                border_width='1',
                trigger_on='mousemove|click',
                formatter=pyecharts.globals.JsCode('''function(parg){\n
                    if( parg.name == '三星')\n
                    {\n
                    return ' 三星： '''+str(len(data_src.wap_3))+' ( '+str(int((len(data_src.wap_3)/total_count)*10000)/100)+''' % )</br>' ;\n
                                

                    }else if (parg.name == '四星武器')\n
                    {\n
                    return ' 四星武器： '''+str(len(data_src.wap_4))+' ( '+str(int((len(data_src.wap_4)/total_count)*10000)/100)+''' % )</br>'+\''''+wap4+'''\' ;\n
                                
                    }else if (parg.name == '五星武器')\n
                    {\n
                    return ' 五星武器： '''+str(len(data_src.wap_5))+' ( '+str(int((len(data_src.wap_5)/total_count)*10000)/100)+''' % )</br>'+\''''+wap5+'''\' ;\n
                                
                    }else if (parg.name == '四星角色')\n
                    {\n
                    return ' 四星角色： '''+str(len(data_src.char_4))+' ( '+str(int((len(data_src.char_4)/total_count)*10000)/100)+''' % )</br>'+\''''+char4+'''\' ;\n
                                
                    }else if (parg.name == '五星角色')\n
                    {\n
                    return ' 五星角色： '''+str(len(data_src.char_5))+' ( '+str(int((len(data_src.char_5)/total_count)*10000)/100)+''' % )</br>'+\''''+char5+'''\' ;\n
                                
                    }\n
                }\n
                                                   '''),
                textstyle_opts=pyecharts.options.TextStyleOpts(font_size=16)
                #添加JS回调函数使数据随鼠标指向的图表变动，展示具体记录
                
                
                ),
            
            
            radius=["35%", "70%"],
            
        )
        .set_global_opts(title_opts=pyecharts.options.TitleOpts(title))
        ).add_js_funcs('''
                       option_defult = {
            
            series: [
                {type:'pie',
                    name:'''+charts_name+''',
                    
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
                       '''+charts_name+'''.setOption(option_defult);''')
        pie.width='720px'
        pie.height ='540px'
        #保存格式化之后的数据
            #替换html换行符

        data_src.wap3_str=re.sub('</br>',r'\n',wap3)
        data_src.wap4_str=re.sub('</br>',r'\n',wap4)
        data_src.wap5_str=re.sub('</br>',r'\n',wap5)
        data_src.char4_str=re.sub('</br>',r'\n',char4)
        data_src.char5_str=re.sub('</br>',r'\n',char5)
        
        return pie


    def dic_to_list(self,dict1):
        
        dictlist=[]
        for keys, value in dict1.items():
            temp = [keys,value]
            dictlist.append(temp)
        return dictlist

    def make_scatter(self):
        wap3=self.dic_to_list(Data.prize().time().time_count_wap_3)
        wap4=self.dic_to_list( Data.prize().time().time_count_wap_4)
        wap5=self.dic_to_list(Data.prize().time().time_count_wap_5 )
        char4=self.dic_to_list( Data.prize().time().time_count_char_4)
        char5=self.dic_to_list( Data.prize().time().time_count_char_5)
        x_data_w3=[]
        x_data_w4=[]
        x_data_w5=[]
        x_data_c4=[]
        x_data_c5=[]
        i=0
        max_w3=[]
        max_w4=[]
        max_w5=[]
        max_c4=[]
        max_c5=[]
        #print(wap3)
        while i<len(wap3):
            if wap3[i][1]!=0:
                x_data_w3.append([wap3[i][0]])
                wap3[i]=[wap3[i][1]]
                max_w3.append(wap3[i][0])
            else:
                
                x_data_w3.append([])
                wap3[i]=[]
                max_w3.append(0)
                #i-=1
            i+=1
        i=0
        while i<len(wap4):
            if wap4[i][1]!=0:
                x_data_w4.append([wap4[i][0]])
                wap4[i]=[wap4[i][1]]
                max_w4.append(wap4[i][0])
            else:
                
                x_data_w4.append([])
                wap4[i]=[]
                max_w4.append(0)
                #i-=1
            i+=1    
        i=0
        while i<len(wap5):
            if wap5[i][1]!=0:
                x_data_w5.append([wap5[i][0]])
                wap5[i]=[wap5[i][1]]
                max_w5.append(wap5[i][0])
            else:
                
                x_data_w5.append([])
                wap5[i]=[]
                max_w5.append(0)
                #i-=1
            i+=1    
        i=0
        while i<len(char4):
            if char4[i][1]!=0:
                x_data_c4.append([char4[i][0]])
                char4[i]=[char4[i][1]]
                max_c4.append(char4[i][0])
            else:
                
                x_data_c4.append([])
                char4[i]=[]
                max_c4.append(0)
                #i-=1
            i+=1    
        i=0
        while i<len(char5):
            if char5[i][1]!=0:
                x_data_c5.append([char5[i][0]])
                char5[i]=[char5[i][1]]
                max_c5.append(char5[i][0])
            else:
                
                x_data_c5.append([])
                char5[i]=[]
                max_c5.append(0)
                #i-=1
            i+=1
        i=0
        x_data=[]
        
        for i in range(24):
            if i <10:
                x_data.append('0'+str(i)+':00' )
                
            else:x_data.append(str(i)+':00')
        #print(x_data_c4)
        #print(char4)
        scatter=(
            pyecharts.charts.Scatter(init_opts=pyecharts.options.InitOpts(chart_id='出货时间分布', theme=pyecharts.globals.ThemeType.MACARONS))
            .add_xaxis( x_data_w3)
            .add_yaxis( '三星',wap3 )    
            .add_xaxis(x_data_w4)
            .add_yaxis('四星武器',wap4)
            .add_xaxis(x_data_c4)
            .add_yaxis('四星角色',char4)
            .add_xaxis(x_data_w5)
            .add_yaxis('五星武器',wap5)
            .add_xaxis(x_data_c5)
            .add_yaxis('五星角色',char5)
            .add_xaxis(x_data)
            .set_global_opts
            (   
            title_opts= pyecharts.options.TitleOpts(title="出货时间分布"),
            visualmap_opts=pyecharts.options.VisualMapOpts(type_="size",max_=max(max_w3+max_w4+max_w5+max_c4+max_c5),min_=1)
            
            )
        )
        scatter.width='640px'
        scatter.height='480px'
        
        return scatter
    def draw(self):
        #绘制日历图
        calend2021=pyecharts.charts.Calendar( init_opts=pyecharts.options.InitOpts(chart_id='calendar2021', width="1160px", height="240px",theme=pyecharts.globals.ThemeType.MACARONS))
        calend2022=pyecharts.charts.Calendar( init_opts=pyecharts.options.InitOpts( chart_id='calendar2022',width="1160px", height="240px",theme=pyecharts.globals.ThemeType.MACARONS))
        
        def takeSecond(elem):
            return elem[1]
 
        Y_data2021={}
        Y_data2022={}
        for k in Data().prize().time().time_all:
            #X_names.append(k)
            if k.split('-')[0] == '2021':
                try:
                    Y_data2021[k.split(' ')[0]]+=1
                except:Y_data2021[k.split(' ')[0]]=1
            elif k.split('-')[0]=='2022':
                try:
                    Y_data2022[k.split(' ')[0]]+=1
                except:Y_data2022[k.split(' ')[0]]=1

        Y_data2021= list(Y_data2021.items())
        Y_data2021.sort(key=takeSecond,reverse=True)
        Y_data2022= list(Y_data2022.items())
        Y_data2022.sort(key=takeSecond,reverse=True)
        ##print(Y_data2022)##
        (
        calend2021
    .add(
        series_name="2021",
        yaxis_data=Y_data2021,
        calendar_opts=pyecharts.options.CalendarOpts(
            pos_left="30",
            
            range_="2021",
            yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False),
        ),
    )
    .set_global_opts(
        title_opts=pyecharts.options.TitleOpts( pos_left="left", title="抽卡分布"),
        visualmap_opts=pyecharts.options.VisualMapOpts(
            max_=Y_data2021[0][1], min_=1, orient="horizontal", is_piecewise=False,pos_left='center',
    
    )        
        ))
        (
        calend2022
    .add(
        series_name="2022",
        yaxis_data=Y_data2022,
        calendar_opts=pyecharts.options.CalendarOpts(
            pos_left="30",
            
            range_="2022",
            yearlabel_opts=pyecharts.options.CalendarYearLabelOpts(is_show=False),
        ),
    )
    .set_global_opts( 
        visualmap_opts=pyecharts.options.VisualMapOpts(
            max_=Y_data2022[0][1], min_=1, orient="horizontal", is_piecewise=False,pos_left='center',
        
    )        
        ))
        #日历图完
        data_src=Data.wapactivity()
        pie1=self.make_pie(data_src, '武器活动祈愿')
        
        data_src=Data.charactivity()
        pie2=self.make_pie(data_src, '角色活动祈愿')
        
        data_src=Data.permanent()
        pie3=self.make_pie(data_src, '常驻祈愿')
        #饼图完
        scatter1=self.make_scatter()
        #散点图完
        global self_path
        page=pyecharts.charts.Page(page_title='山泽麟迹', layout=pyecharts.charts.Page.DraggablePageLayout)
        page.add(pie1,pie2,pie3,calend2021,calend2022,scatter1).render('./TEST.html')#添加图表
        #page.add(pie1,pie2,pie3).render('TEST.html')#添加图表,不含日历图
        page.save_resize_html('./TEST.html',cfg_file='./chart_config.json',dest=self_path+'/山泽麟迹.html')
        os.remove( './TEST.html')
        #需要改变图表布局则屏蔽这两行，在测试网页里保存配置(*.json)，或者直接修改
        
    



    def data_clean(self,class_,st):#数据筛选
        if st['item_type'] == '武器':
            if st['rank_type']=='5':
                class_.wap_5.append( st)
                Data.prize().time().time_wap_5.append( st['time'])
                Data.prize().id().id_wap_5.append(st['id'])
            elif st['rank_type'] =='4':
                class_.wap_4.append(st)
                Data.prize().time().time_wap_4.append( st['time'])
                Data.prize().id().id_wap_4.append(st['id'])
            else:
                class_.wap_3.append(st)
                Data.prize().time().time_wap_3.append( st['time'])

        if(st['item_type']) == '角色':
            if st['rank_type'] =='5':
                class_.char_5.append(st)
                Data.prize().time().time_char_5.append( st['time'])
                Data.prize().id().id_char_5.append(st['id'])
            else:
                class_.char_4.append(st)
                Data.prize().time().time_char_4.append( st['time'])
                Data.prize().id().id_char_4.append(st['id'])

    
    def data_process(self):
        ensure_count_200,ensure_count_100,ensure_count_302,ensure_count_301=0,0,0,0
        data_all=Data().alldata
        for data in data_all:
            #print(data)
            for sth in data:

                class_buf=None
                #数据遍历开始
                #sth['ensure_count']=data.index(sth)+1#标记出货位置##错误的标记方式
                self.prize().time().time_all.append(sth['time']) #处理时间
                #print(sth)
                #输出状态
                if(sth['gacha_type']=='200'):#常驻祈愿
                    class_buf=Data.permanent()#更改类
                    Data.data_clean(self, class_buf, sth)#筛选数据
                    sth['ensure_count']=ensure_count_200+1#标记出货位置
                    ensure_count_200+=1
                    #print("正在处理 常驻祈愿 "+str(data.index(sth)+1)+' / '+str(len(data)))
                elif(sth['gacha_type']=='100'):#新手祈愿
                    class_buf=Data.novice()#更改类
                    Data.data_clean(self, class_buf, sth)#筛选数据
                    sth['ensure_count']=ensure_count_100+1#标记出货位置
                    ensure_count_100+=1

                    #print("正在处理 新手祈愿 "+str(data.index(sth)+1)+' / '+str(len(data)))
                elif(sth['gacha_type']=='301'or sth['gacha_type']=='400'):#角色活动祈愿
                    class_buf=Data.charactivity()#更改类
                    Data.data_clean(self, class_buf, sth)#筛选数据
                    sth['ensure_count']=ensure_count_301+1#标记出货位置
                    ensure_count_301+=1
                    #print("正在处理 角色活动祈愿 "+str(data.index(sth)+1)+' / '+str(len(data)))
                elif(sth['gacha_type']=='302'):#武器活动祈愿
                    class_buf=Data.wapactivity()#更改类
                    Data.data_clean(self, class_buf, sth)#筛选数据
                    sth['ensure_count']=ensure_count_302+1#标记出货位置
                    ensure_count_302+=1
                    #print("正在处理 武器活动祈愿 "+str(data.index(sth)+1)+' / '+str(len(data)))

class Request():

    def __init__(self):
        {}
 
    def request(self,src_url,typecode,data_old=None):
        pagecount,endid=0,0
        list_buf=[]
        while True:
            response=requests.get(Log().trans_url(src_url,typecode,pagecount,endid))
            #print(response.text)
            try:
                if(response.text.index('visit too frequently')):
                    time.sleep(0.5)#防止请求频繁
                    continue
            except:{}
            pagecount+=1#页码4
            if  'null' in response.text:
                #print (response.text)
                raise Exception(str(typecode)+response.text[24:39])
            list_buf= eval(response.text)['data']['list']#字典化
            #print(list_buf)

            if list_buf==[]:break#为空则跳出

            #否则赋值给数据类中对应列表
            if(typecode==200):#常驻祈愿
                print("获取 常驻祈愿 "+str(pagecount)+' 页')
                for sth in list_buf:
                    Data.permanent_data.append(sth)
            elif(typecode==100):#新手祈愿
                print("获取 新手祈愿 "+str(pagecount)+' 页')
                for sth in list_buf:
                    Data.novice_data.append(sth)
            elif(typecode==301 or typecode==400):#角色活动祈愿
                print("获取 角色活动祈愿 "+str(pagecount)+' 页')
                for sth in list_buf:
                    Data.charactivity_data.append(sth)
            elif(typecode==302):#武器活动祈愿
                print("获取 武器活动祈愿 "+str(pagecount)+' 页')
                for sth in list_buf:
                    Data.wapactivity_data.append(sth)

            endid=list_buf[len(list_buf)-1]['id']#刷新ID
            if len(list_buf)!=20:break#最后一页跳出

def main():
    global self_path
    Log().get_log()
    Request().request( Log().get_url(),200)#常驻祈愿
    Request().request( Log().get_url(),100)#新手祈愿
    Request().request( Log().get_url(),301)#角色活动祈愿
    Request().request( Log().get_url(),302)#武器活动祈愿
    #print(Data.charactivity_data)
    #print(Data.wapactivity_data)
    Data().data_process()
    #print(Data.charactivity().char_5)
    Data().prize_count()
    #print(Data().wapactivity().ensure_list)
    #print(Data().prize().charactivity().average_pro_5)
    #print(Data().prize().time().time_all)
    Data().draw()
    Save.Save_all_data(Data)
    webbrowser.open(self_path+"/山泽麟迹.html")

main()
#except Exception as e:open('log.txt', 'a',encoding='utf-8').writelines('\n'+str(e))