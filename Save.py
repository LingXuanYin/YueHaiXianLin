import os
import glob
import re

def Save_all_data(src_data,path=os.getcwd()):
    uid_new=src_data[0]['uid'] 
    uid_old=[]
    file_old=[]
    list_old=[]
    for file in glob.glob("*.txt"):
        if "藏弓待用" in file:
           file_old.append(path+'/'+file)
           uid_old.append(eval(open(path+'/'+file,'r',encoding='utf-8').readline())[0]['uid'])
    if uid_new in uid_old:
        list_old=eval(open(path+'/'+'藏弓待用'+uid_new+'.txt','r',encoding='utf-8').readline())
        for sth in src_data:
            if sth not in list_old:
                list_old.append(sth)
       
        open(path+'/'+'藏弓待用'+uid_new+'.txt',"w+",encoding="utf-8").writelines(str(list_old))
    else :
        open(path+'/'+'藏弓待用'+uid_new+'.txt',"w+",encoding="utf-8").writelines(str(src_data))
    
    
def Read_all_data(uid,path=os.getcwd()):
    return eval(open(path+'/'+'藏弓待用'+uid+'.txt',"r",encoding="utf-8").readline())
    