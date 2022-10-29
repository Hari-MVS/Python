first_word=input()
second_word=input()
string=''
i=len(first_word)-1
while i>0:
    if second_word.startswith(first_word[i:]):
        string+=first_word[i:]
        break
    i-=1
print(string if string else 'No overlapping')
    
