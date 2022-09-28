a=input()
b=input()
print("Allowed to write exam" if int(a[0:-1])>=75 or 
(int(a[0:-1])<75 and b=="Y") else ("Cannot write exam"))
