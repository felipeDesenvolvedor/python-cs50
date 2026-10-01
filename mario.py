table = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
]

for lines in table:
    for line in lines:
        if line == 0: 
            print(line, end="")
        else: 
            print(1, end="")
    print()        
