import os
import glob
import re

def Save_all_data(src_data,path=os.getcwd()):
    list_old=[]
    list_new=[]
    file_old,file_new="",""
    start_time=sorted(src_data.prize().time().time_all)[0]
    end_time=sorted(src_data.prize().time().time_all,reverse=True)[0]
    start_time= start_time.split(" ")[0]
    end_time= end_time.split(" ")[0]
    #print(start_time,end_time)
    for file in glob.glob("*.txt"):
        if "藏弓待用" in file:
            file=path+"/"+file
            list_old= eval(open(file,"r",encoding="utf-8").read())
            file_old=file
            #print(file_old,file)
    file_new=path+"/藏弓待用"+start_time+"——"+end_time+".txt"
    open(file_new,"w+",encoding="utf-8").writelines(str(src_data.charactivity_data+src_data.wapactivity_data+src_data.permanent_data+src_data.novice_data))
    list_new= eval(open(file_new,"r",encoding="utf-8").readline())
    #print(str(src_data.charactivity_data+src_data.wapactivity_data+src_data.permanent_data+src_data.novice_data))
    
    #print(list_new)
    for new in list_new:
        if new not in list_old:
            list_old.append(new)
    
    open(file_new,"w+",encoding="utf-8").writelines(str(list_old))
    if os.path.exists(file_old)and file_old!=file_new:
        os.remove(file_old)
    
            
    
    
    