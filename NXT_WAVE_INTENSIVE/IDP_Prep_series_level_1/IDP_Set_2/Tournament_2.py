n=int(input())
for i in range(n):
    m=int(input())*100
    d={'M':0,'D':0,'A':0}
    for i in input():
        if i in d:
            d[i]+=1
    if d["A"]>d["M"]:
        print(int(40/100*m))
    elif d["M"]>d["A"]:
        print(int(60/100*m))
    elif d["A"]==d["M"]:
        print(int(55/100*m))
        
    


