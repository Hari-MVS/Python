a = input()
sum=0
for i in a:
    sum+=int(i)**len(a)
print("Armstrong Number" if sum==int(a) else "Not an Armstrong Number")
