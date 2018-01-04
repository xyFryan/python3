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
