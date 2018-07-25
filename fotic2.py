#此脚本测试多个页面是否可以访问
import requests
import os
import re
ulist = []
#get_file方法获取url参数通过flist收取
def get_file():
   f = open("F:/foticpython/url.txt","r+")
   for file in f.readlines():
        ulist.append(file.strip())
   f.close()
get_file()
for url in  ulist:
  try:
     req = requests.get(url,timeout=1.5)
  except requests.exceptions.Timeout:
      u = re.findall(r'\d+.\d+.\d+.\d+:\d+', url)
      u = u[0]
      print("%s环境服务不正常,IP:%s" % (u, url))
      continue
  u  = re.findall(r'\d+.\d+.\d+.\d+:\d+', url)
  u  = u[0]
  print("%s环境服务正常,IP:%s状态码:%s"%(u,url,req.status_code))










