# dzinf
# 2 Задание
def Imp(x, y):
    return not x or y
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = Imp(w, y) and (not (y) == x) and (x or z)
                if not f:
                    print(x, y, z, w)

#Ответ: xzwy

# 5 Задание
for i in range(10000, 100000):
    n = str(i)
    c1 = int(n[0]) + int(n[2]) + int(n[4])
    c2 = int(n[1]) + int(n[3])
    one = str(min(c1, c2))
    two = str(max(c1, c2))
    r = one + two
    if r == '621':
        print(i)
        break
#Ответ: 30969

# 8 Задание
k = 0
from  itertools import *
a = product('АКРУ', repeat=5)

for x in a:
    s = "".join(x)
    k += 1
    if s[0] == 'К':
        print(k)
        break
#Ответ: 257

# 9 Задание
k = 0
f = open('scratch_184.txt')
for i in f.readlines():
    i = i.replace(',', '.')
    a = list(map(float, i.split()))
    mini = min(a)
    sr = sum(a) / len(a)
    if sr - mini >= 8:
        k += 1
print(k)
#Ответ: 51

# 12 Задание
s = '1' + '9' * 98
while ('19' in s) or ('299' in s) or ('3999' in s):
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)
#Ответ: 29

# 14 Задание
f = 4 ** 12 + 2 ** 32 - 16
n = bin(f)[2:]
print(n.count('1'))
#Ответ: 21

# 15 Задание
def F(a):
    for x in range(0, 500):
        for y in range(0, 400):
            f = (y + 2 * x < a) or (x > 15) or (y > 30)
            if not f:
                return False
    return True

for a in range(0, 400):
    if F(a):
        print(a)
        break
#Ответ: 61

# 16 Задание
def F(n):
     if n == 1:
         return 1
     elif n == 2:
         return 1
     elif n > 2:
         return F(n - 2) + F(n - 1)

print(F(9))
#Ответ: 34

# 17 Задание
f = open('scratch_180.txt')
a = [int(i) for i in f.readlines()]
k = 0
maxi = -100000000

for i in range(len(a)):
    for g in range(i + 1, len(a)):
        if (a[i] + a[g]) % 60 == 0:
            if a[i] % 40 == 0 or a[g] % 40 == 0:
                k += 1
                maxi = max(maxi, a[i] + a[g])
print(k, maxi)
#Ответ: 29278 19860

# 23 Задание
def F(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x == 16:
        return 0
    else:
        return F(x + 1, y) + F(x * 2, y)

print(F(1, 10) * F(10, 21))
#Ответ: 14

# 24 Задание
f = open("C:\\Users\\79049\Downloads\\24.txt")
a = f.readline().split('E')
maxi = 0

for i in a:
    if i.count('A') >= 3:
        maxi = max(len(i), maxi)
print(maxi)
#Ответ: 275

# 25 Задание
def M(x):
    b = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            b.append(i)
    if len(b) != 0:
        return max(b) + min(b)
    else:
        return 0


k = 0
for i in range(700000, 800001):
    if M(i) % 10 == 8:
        k += 1
        print(i, M(i))
        if k == 5:
            break
#Ответ: 700005 233338
#       700007 100008
#       700012 350008
#       700015 140008
#       700031 24168

