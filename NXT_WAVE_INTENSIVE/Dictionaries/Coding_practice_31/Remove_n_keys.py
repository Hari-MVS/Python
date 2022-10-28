alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

a=input().split()
for i in a:
    if i in alphabets:
        del alphabets[i]

# a=input().split()
# re={i:j for i,j in alphabets.items() if i not in a}
print(alphabets)
