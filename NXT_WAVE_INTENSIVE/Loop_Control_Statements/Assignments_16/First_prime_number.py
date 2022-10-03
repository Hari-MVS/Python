
num = int(input())
        
flag = False
first_prime =0
for i in range(1,num+1):
    sec = int(input())
    flag= False
    if(sec==1):
        continue
            
    for j in range(2,sec+1):
        if (sec==j):
            break
        elif (sec%j==0):
            flag= True
                
            
            
    if (flag == False):
        print(sec)
        break
