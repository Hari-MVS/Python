a=input()
for i in range(len(a)):
    if a[i].isdigit():
        print(a[i:])
        break
