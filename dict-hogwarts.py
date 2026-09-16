students = {"Hermione":"Gryffindor", "Harry":"Gryffindor", "Ron":"Gryffindor"}

for stutend in students:
    print(stutend, students[stutend], sep=", ")


students2 = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
] 

for student in students2:
    print(student["name"], student["house"], student["patronus"], sep=", ")
