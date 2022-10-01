a = input()
password = ""
for i in a:
    if i.isupper():
        password="Valid Password"
        break
    else:
        password="Invalid Password"
print(password)
