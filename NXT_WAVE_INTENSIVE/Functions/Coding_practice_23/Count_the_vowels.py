def count_the_vowels(word):
    vow=('a','e','i','o','u','A','E','I','O','U')
    count=0
    for i in word:
        if i in vow:
            count+=1
    return count


word = input()
print(count_the_vowels(word))
