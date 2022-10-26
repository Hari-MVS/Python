fir=[int(i) for i in input().split()]
sec=[int(i) for i in input().split()]
th=[int(i) for i in input().split()]

tem=set(fir).intersection(set(sec))
print(list(set(th).intersection(tem)))
