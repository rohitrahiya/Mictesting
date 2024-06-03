
for i in range(1,8):
    for j in range(1,15):
        if j>=8-i and j<=6+i:
            print("*", end='')
        else:
            print(" ", end='')
    print()

for i in range(1,10):
    for j in range(1,14):
        if j>=0+i and j<=14-i:
            print("*", end='')
        else:
            print(" ", end='')
    print()