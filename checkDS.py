#coding:utf-8
import os,re
from test101 import dy
file = open(r'D:\Program Files (x86)\Jenkins\jobs\CheckDS\nextBuildNumber','r+')
test = file.readlines()
for i in test:
    num = (int(i)-1)
test = r"D:/Program Files (x86)/Jenkins/jobs/CheckDS/builds" + r"/" + str(num) + r"/log"
file = open(test,'r+')
getlist = []
for f in file.readlines():
        if re.match('\d+',f):
            getlist.append(f)
            print(f)

file.close()
getlist1 = []
for i in getlist:
               if int((i.split('%')[0].split(':')[1])) > 96:
                                dy(((i.split('%')[0])[:11]))
#              getlist1.append((i.split('%')[0].split(':')[1])
#print (getlist1)
#for j in getlist1:
#              if  int(j) > 80:
#                  dy(j)

