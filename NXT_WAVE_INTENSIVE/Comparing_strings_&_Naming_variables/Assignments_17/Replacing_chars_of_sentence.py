m = input()
ne=""
for i in range(0,len(m)):
    if (m[i]==" "):
        ne+=" "
    else:
        ne+=(chr(ord(m[i])+1))
            
        
print(ne)
