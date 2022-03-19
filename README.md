# YueHaiXianLin
#说明：

#这是一个可以一键查询原神抽卡记录（六个月内）并可视化的脚本
#支持自动保存并合并历史记录

# 使用方法：

# 如果你只是想简单使用该脚本，则只需下载 月海仙麟v*.*.*.exe 并参照以下方法使用：
#     登录原神对应账号并打开祈愿历史记录-->退出游戏启动此脚本

# 问题解决：

    #运行后闪退：
        #拖到cmd或者powershell中执行：
            #报错：
#                 Failed to establish a new connection: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试：
#                    关闭杀软（包括火绒和wdf）或者加白并允许访问互联网
                 #其他：
                    #尝试以win7兼容性模式+管理员权限运行
    #运行后报错：
        #*** 不可用/请求为空：
            #链接失效，删除文件夹内output_log.txt，重复使用方法
        #其他：
            #按照报错提示进行或
#            联系开发者 （QQ：3546599908  群：777974176）
#2022/3/19   v1.0.1 

#更新内容：
    #增加了保底重置计数
    #重构了代码，增添注释
    #修改了可视化逻辑，大部分使用pyecharts进行
    #更改了网页结构，增添日历热力图和散点图
    #支持自定义网页结构（chart_config.json）
    #修改应用图表和部分文件命名
    #增添了自动保存和合并抽卡记录（目前仅支持2021-2022年）
        #记录保存格式为  [ { 'get到的单行数据' },{...},{...} ]
    #保存在程序所在目录的 藏弓待用'开始日期'——'截止日期'.txt
    
            #v1.0.0
#实现思路：
#通过原神内置浏览器的日志文件获取抽卡查询链接
#使用request库的get方法得到抽卡记录数据
#将数据以源码形式直接注入网页
#调用echarts实现可视化
#网页较为简陋  丞待完善

