""" def greater_char(str):
    word_splt = str.split()
    count = 0
    for i in word_splt:
        dic = {}
        for j in i :
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] +=1
            if dic[j] >= count :
                count = dic[j]
                repet_char = i
    return repet_char

print(greater_char(input('Enter a string : '))) """


def char(arr):
    count =0
    chr_len = arr.split()
    for i in chr_len:
        dic ={}
        
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j]+=1
            if dic[j] >= count :
                count = dic[j]
                rep_char = i
        
    return rep_char

print(char(input('Enter any string : ')))
            
