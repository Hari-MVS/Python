programming_languages = ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl', 'R', 'Swift', 'SQL', 'PHP', 'JavaScript']
n=int(input())
print(programming_languages if n==0 else programming_languages[:(-n)])
