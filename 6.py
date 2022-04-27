
#1
n = int(input("Введите n : "))
e = 0
while(e < n):
   e = e + 1
   print(e)
print()

#2
a = 9
while(a < 99):
   a = a + 2
   print(a)
print()

#3
a = int(input(" : "))
b = 0
while a % 10 != 0:
    b = b + a % 10
    a = int(a / 10)
print(b)

#4
a = int(input("do cuda cvadrat : "))
b = 0
while(b * b <= a):
   print(b,"*",b,"=",b*b)
   b = b + 1
print()

#5
a = int(input("do cuda : "))
i = 1
n = 3
while(i < a):
   print(i)
   i = i + n
   n = n + 2
print()

#6
a = 1.0
while(a <= 13.5):
   print(a)
   a = a + 0.5
print()

#7
a = float(input("0 < a < 1 : "))
b = 1
while(a < (1/b)):
    b+=1
    print("1 /",b)
print()

#8
a = float(input("1 < a < 1.5 : "))
b = 1
while(a < 1+(1/b)):
    b+=1
    print("1 + 1/",b,sep="")
print()

#9
from itertools import dropwhile
l = list(map(int, input('posledovatelnost :' ).split(' ')))
print(sum(dropwhile(lambda x: x<0, l)))
print()

#10
a = [1,2,3,4,5,0,6,7,8,9]
b = 0
while(a[b] != 0):
      b = b + 1;
print(b)
print()

#11
a = ["1","2","3","4","5","6","7","8","9"]
i = 0
k = 0
while(int(a[i])%2):
    k += int(a[i])
    i += 1
print(k)

#12
l = [1,2,3,4,5,1,2,3,4,5,6]
print(len(l) - len(set(l)))
print()

#13
a = 0
while(a<6000000):
    a = a + 1
print("end zaderzka")
print()

#14
a = int(input("vvedite chetnoe chislo : "))
while(a%2):
    print("you stupid?")
    a = int(input("vvedite chetnoe chislo : "))
print("molodec")
print()

#15
a = int(input("vvedite password : "))
while(a != 6539):
    print("ne tot")
    a = int(input("vvedite password : "))
print("vi v sisteme")
print()

#16
b = 0
while(b != 10):
    b = b +1
    a = int(input("chislo : "))
    if (a == 0):
        print("a vso, bolshe nelzya")
        break
print("konec")
print()

#17
n = int(input("chislo : "))
for t in range(1,n):
    if t ** 2 > n:break
print(t)
print()

#18
a = float(input("chislo 0 < a =< 1 : "))
i = 1
while(1/i >= a):
   print("1/"+str(i))
   i += 1
print()

#19
for t in range(0,21):
    print(100 - i)
print()
a = 100
while(79 < a):
    print(a)
    a -= 1
print()

#20
for i in range(2,16):
    print((i * 10 + 1) * 2)
print()

#21
n=2
for t in range(0,21):
    print(n)
    n +=0.5
print()

#22
m = float(input("chislo 0.52 < a =< 33,7 : "))
for x in range(1,101):
    y = ((x*x) + 100)/(x + 200)
    if(m>y):
        print(y)
    else:
        break
print()

#23
m = float(input("chislo 0.5 < a =< 1 : "))
x = 1
y = 2
while(m > x/y):
    print(x,"/",y, sep="")
    x += 1
    y += 1
