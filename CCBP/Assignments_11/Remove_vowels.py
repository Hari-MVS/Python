a = input()
vowels=("a","e","i","o","u","A","E","I","O","U")
s=a
for i in range(len(a)):
    if a[i] in vowels:
        
        s=s.replace(a[i],"")
print(s)
