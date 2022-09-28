m=int(input())
p=int(input())
c=int(input())
if ((m >=60 and p >=50 and c>=45) and ((m+p+c) >=180)) 
or ((m+p)>=120 or (c+p)>=110):
    print("True")
else:
    print("False")
