import re
url = "http://10.7.101.120:9087/contract/reminiscenceLogin.html#"
print (re.findall(r'\d+.\d+.\d+.\d+:\d+',url))
