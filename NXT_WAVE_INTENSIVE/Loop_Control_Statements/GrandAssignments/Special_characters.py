user = input()
vowel = ('a','e','i','o','u','A','E','I','O','U')
vow=0
consonant =0
for i in user:
    if i in vowel:
        vow+=1
    elif (i==" ") :
        continue
    else:
        consonant+=1
print(vow)
print(consonant)
