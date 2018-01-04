#!/usr/bin/python3
fav_movies=["The Holy Grail","The Life of Brain"]
#for opt in list
print("这里是用for循环:")
for each_flick in fav_movies:
    print(each_flick)
count = 0
print("这里是用while循环:")
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1
#isinstance(object, classinfo)
names = ["Michael","Terry"]
a=isinstance(names,list)
print(a)
#a=true print false ,a=false print true
if a:
    print("false")
else:
    print(a)
movies=["The Holy Grail",'1975',"The Life of Brain",'91',["Graham Chapman","Micheal Palin",'John Cleese']]
'''
def 函数名 (参数):
    函数代码组
'''
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)