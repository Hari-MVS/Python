a = input()
password = ""
for i in a:
    if i.isdigit():
        password="Valid Password"
        break
    else:
        password="Invalid Password"
print(password)
