#!/usr/bin/python3
cast=["Cleeese",'Palin','Jones',"Idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("Galliam")
print(cast)
print(cast.pop())
print(cast)
print("增加\"Gilliam\",\"Chapman\"")
cast.extend(["Gilliam","Chapman"])
print(cast)
print("删除\"Chapman\"")
cast.remove("Chapman")
print(cast)
print("增加\"Chapman\"到0的位置")
cast.insert(0,"Chapman")
print(cast)
