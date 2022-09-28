def closest_zero(arr):
    positive = [] 
    negative = []
    if len(arr) == 0:
        print('0')
    else:
        for i in arr:
            if i >= 0 :
                positive.append(i)
            else:
                negative.append(i)
    return min(positive) if min(positive) + max(negative) < 0 else max(negative)
        #print(min(postive))
    #else:
        #print(max(negative))
        
print(closest_zero([4, 1, 88, 44, 3,-1,-7,-19,-0.5,-0.2]))

