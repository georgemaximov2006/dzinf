# dzinf
# №106
for x in range(100, 10, -1):
    y = str(x % 4) + str(x % 2) + str(x % 5)
    if y == '202':
        print(x)
        break
#Ответ: 82

# №107
k = 0
for x in range(10, 100):
    y = str(x % 4) + str(x % 2) + str(x % 3)
    if y == '201':
        k += 1
print(k)
#Ответ: 8

#108
k = 0
for x in range(10, 100):
    y = str(x % 4) + str(x % 3) + str(x % 2)
    if y == '200':
        k += 1
print(k)
#Ответ: 7

#109
k = 0
for x in range(10, 100):
    y = str(x % 7) + str(x % 2) + str(x % 5)
    if y == '312':
        k += 1
print(k)
#Ответ: 2
