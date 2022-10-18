def get_lower_and_upper_case_letters(word):
    up=''
    lo=''
    for i in word:
        if i.isupper():
            up+=i
        else:
            lo+=i
    return up,lo


word = input()
a,b=get_lower_and_upper_case_letters(word)
print(a)
print(b)
