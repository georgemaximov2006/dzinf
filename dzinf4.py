#5 Задание
for i in range(1, 100):
    n = bin(i)[2:]
    n += n[-1]
    n += n[-1]
    r = int(n, 2)
    if r > 123:
        print(r - 1)
        break
  #Ответ: 126

#8 Задание
k = 0
from itertools import *
a = product('АВСХ', repeat=5)

for x in a:
    s = "".join(x)
    if not 'Х' in s[0:4]:
        k += 1
print(k)
#Ответ: 324
