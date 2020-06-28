import os, sys
import glob
import re
from shutil import copyfile
from sys import exit

if os.path.exists("name1.txt"):
    os.remove("name1.txt")
if os.path.exists("name2.txt"):
    os.remove("name2.txt")
    
getfile_name = input("Please input file format:")
#----------------------------------获取文件数量-----------------------------*
def getnumber(getfile_name):
    global number
    path_file_number=glob.glob(pathname='*'+ getfile_name) #获取当前文件夹下个数
    print("识别到的文件数量为:",len(path_file_number),"\n")
    number = len(path_file_number)
    
getnumber(getfile_name)

#-------------------------------识别文件名字并且输出为txt--------------------
def file_name(file_dir,getfile_name):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == getfile_name:  
                #L.append(os.path.join(root, file))  
                file_name = file[0:-4]  #去掉后缀
                L.append(file_name)  
    return L  
    
label_folder = "./"
trainval_file = "name1.txt"

txt_name = file_name(label_folder,getfile_name)

with open(trainval_file, "w") as f:
  for i in txt_name:
    f.write("{}\n".format(i))
    print("{}\n".format(i))
f.close()
#-------------------------------识别第几集并且写出-----------------------------------

string = open("name1.txt")

def doresult():
    line = string.readline()
    result = line
    result = re.sub("[Ss]+[0-9]+[0-9]*","",str(result))
    result = re.sub("[0-9][0-9][0-9][0-9]","",str(result))
    result = re.sub("[0-9][0-9][0-9]","",str(result))
    #result = re.search(r"([^0-9][0-9][0-9][^0-9])",result)
    result = re.search(r"([0-9]*[0-9])",result)
    renumber = result.group(1)
    print(renumber)
    with open("name2.txt","a") as f:
        f.write(renumber+"\n")
print("以下为匹配到的集数请检查:")   
for i in range(number):
    doresult()

#--------------------------重命名---------------------------------

def dorename(number):
    name1path = open("name1.txt")
    name2path = open("name2.txt")
    for i in range(number):
        linename1 = name1path.readline()
        linename1 = re.sub("\\n","",str(linename1))
        linename2 = name2path.readline()
        linename2 = re.sub("\\n","",str(linename2))
        if os.path.exists(linename1+getfile_name):
            print("匹配到:"+linename1+getfile_name + "  开始重命名")
            os.rename(linename1+getfile_name , "["+linename2+"]"+getfile_name)
            print(linename1+getfile_name + "-->"+"["+linename2+"]"+getfile_name)
        else:
            print("匹配:"+linename1+getfile_name + "  失败")
if input("input Yes to rename:") == "Yes":
    dorename(number)
    input("输入任意键退出")
else:
    input("输入任意键退出")
    
    
    
