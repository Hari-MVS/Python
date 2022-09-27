T= float(input())
if T<0:
    print("Freezing weather")
else :
    if ((0<=T) and (T<10)):
            print("Very Cold weather")
    else :
        if ((10<=T) and (T<20)):
            print("Cold weather")
        else: 
            if ((20<=T) and (T<30)):
                print("Normal")
            else : 
                if ((30<=T) and (T<40)):
                    print("Hot")
                else:
                    print("Very Hot")
        
