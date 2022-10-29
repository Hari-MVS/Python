string=[i for i in input().split()]
word_count={}
for i in string:
    if i not in word_count:
        word_count[i]=1
    else:
        word_count[i]+=1

for i in word_count:
    print(i+':',word_count[i])
