a= input()
b= int(input())
day =0
if a=="Monday":
    day=1
if a=="Tuesday":
    day=2
if a=="Wednesday":
    day=3
if a=="Thursday":
    day=4
if a=="Friday":
    day=5
if a=="Saturday":
    day=6
if a=="Sunday":
    day=7
target_day = (day+(b-1))%7
print("Monday" if target_day==1 else ("Tuesday" if target_day==2 else 
("Wednesday" if target_day==3 else ("Thursday" if target_day==4 
else ("Friday" if target_day==5 else("Saturday" if target_day==6 else "Sunday"))))))
