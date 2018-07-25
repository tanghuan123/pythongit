#此脚本初步测试页面是否可以访问并有返回值
import requests
#url = "http://10.7.101.43:9082/contract/reminiscenceLogin.html#"
url = "http://10.7.101.47:9080/contract/reminiscenceLogin.html#"
try:
  req = requests.get(url,timeout=1.5)

except requests.exceptions.Timeout:
    print("no")
