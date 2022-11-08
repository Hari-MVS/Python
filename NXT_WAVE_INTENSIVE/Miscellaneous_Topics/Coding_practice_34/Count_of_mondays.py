import datetime
n=input().split()
dif=[i for i in range(int(n[0]),int(n[1])+1)]
count=0
for i in dif:
    for j in range(1,12+1):
        tem=datetime.datetime(i,j,1)
        if tem.strftime('%A') == 'Monday':
            count+=1
print(count)

