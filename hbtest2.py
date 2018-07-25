list1 = []
list2 = []
list3 = []
#打开文件test1，将test1文件写入列表list1中
with open('test1.txt', 'r') as f1:
    for i in f1.readlines():
        list1.append(i)
#对list1列表里面的每一个字符串元素转成列表使用list2进行接收
    for j in range(len(list1)):
        for k in list(list1[j].strip()):
            list2.append(k)
list1 = []
with open('test2.txt', 'r') as f2:
    for i in f2.readlines():
        list1.append(i)
    for j in range(len(list1)):
        for k in list(list1[j].strip()):
            list3.append(k)
#两个列表组成字典
dt = dict(zip(list2, list3))
#将字典写入文件，并设置换行符标志
with open('test3.txt', 'w') as f3:
    i = 1
    for k, v in dt.items():
                   f3.write(k)
                   f3.write(v)
                   if i % 3 ==0:
                       f3.write('\n')
                   i = i + 1


