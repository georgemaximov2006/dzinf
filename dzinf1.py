# dzinf
# №106
for x in range(100, 10, -1):
    y = str(x % 4) + str(x % 2) + str(x % 5)
    if y == '310':
        print(x)
        break
