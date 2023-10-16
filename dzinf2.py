# dzinf2
#Задача 1
def F(a):
    for x in range(0, 500):
        for y in range(0, 500):
            f = (2 * x + 3 * y != 60) or (a >= x) or (a >= y)
            if not f:
                return False
    return True

for a in range(0, 400):
    if F(a):
        print(a)
        break
#Ответ: 12

#Задача 2
def F(a):
    for x in range(0, 500):
        for y in range(0, 500):
            f = (y + 2 * x < a) or (x > 15) or (y > 30)
            if not f:
                return False
    return True

for a in range(0, 400):
    if F(a):
        print(a)
        break
#Ответ: 61

#Задача 3
def F(a):
    for m in range(0, 500):
        for n in range(0, 500):
            f = (2 * m + 3 * n > 40) or ((m < a) and (n <= a))
            if not f:
                return False
    return True

for a in range(0, 400):
    if F(a):
        print(a)
        break
#Ответ: 21
