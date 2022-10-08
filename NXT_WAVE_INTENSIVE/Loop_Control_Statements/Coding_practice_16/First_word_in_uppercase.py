num = input()
word = ""
        
for i in range(0,len(num)):
    word+=num[i].upper()
    if num[i] == ' ' :
        word+=num[i+1:]
        break
            
        
print(word)
