a= input()
b=int(input())
print('True' if a[:b] != a[-b:] else 'False')
