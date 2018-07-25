list1 = []
list2 = []
with open('test1.txt','r') as f1:
    for i in f1.readlines():
        list1.append(i)
    list2 = list(list1[0].strip())
    for i in list(list1[1]):
        list2.append(i)
    print(list2)