a = input()
b= a.replace(" ","")
c=b.replace("'","")

print("True" if (c.lower()) == (c[::-1].lower()) else "False")
