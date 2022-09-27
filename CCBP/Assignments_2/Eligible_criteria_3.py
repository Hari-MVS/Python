m=int(input())
p=int(input())
c=int(input())
if (m >= 35 and p >=35 and c >=35) and ((m+p) >=90 or (m+c) >=90):
    print("True")
else:
    print("False")
