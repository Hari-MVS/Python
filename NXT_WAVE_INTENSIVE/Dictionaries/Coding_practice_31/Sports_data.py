students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

for i in range(int(input())):
    a,b=input().split()
    students_dict[a]=b
print(students_dict)
