num = int(input())
sec = int(input())
count=0
        
        
for i in range(num,sec+1):
    count=0
    for j in range(2,sec+1):
        if (i%j==0 ):
            count+=1
                
            
    if (count>1):
        print(i)
