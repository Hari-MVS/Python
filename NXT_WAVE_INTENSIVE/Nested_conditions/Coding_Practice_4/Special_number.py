s = input()
print("Special Number" if int(s[0])==7 or int(s[1])==7 
or (int(s[0])+int(s[1])==7) or int(s)%7==0 else "Normal Number")
