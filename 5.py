
#1
import turtle

turtle.speed(30)
turtle.penup()
turtle.fd(-150)

turtle.pendown()
for i in range(4):
   turtle.fd(50)
   turtle.right(90)

turtle.penup()
turtle.right(-90)
turtle.fd(50)

turtle.pendown()
for i in range(6):
    turtle.fd(30)
    turtle.right(60)

turtle.penup()
turtle.fd(50)
turtle.right(90)

turtle.pendown()
for i in range(12):
    turtle.fd(20)
    turtle.right(-30)

turtle.penup()
turtle.fd(200)

turtle.pendown()
for i in range(20):
    turtle.fd(15)
    turtle.right(-18)

turtle.penup()
turtle.right(90)
turtle.fd(50)

turtle.speed(400)
turtle.pendown()
for i in range(360):
    turtle.fd(1)
    turtle.right(1)

#2
a = int(input("кубы всех чисел от 10 до : "))
for t in range(10,a):
   print(t,"в кубе =",t * t * t)
print()

#3
print("фунт   кг")
for t in range(11):
   print(t,"    ",t * 0.453)
print()

#4
for t in range(11):
   print(t,"* 7 =",t*7)
print()

#5
a = -1
for t in range(10,100,2):
      print(t)
for t in range(10,60):
    a = a + 2
    print(a)
print()

#6
for t in range(10,100):
    if(t%10 == 7 or t%10 == 3):
        print(t)
print()

#7
NMin = int(input("от : "))
NMax = int(input("до : "))
Crat = int(input("кратное : "))
for t in range(NMin,NMax+1):
    if(t%Crat == 0):
        print(t)
print()

#8
for t in range(10,100):
    if(((int(t/10) * int(t/10))+((t%10)*(t%10)))%13==0):
        print(t,":",int(t/10) * int(t/10),"+",((t%10)*(t%10)),"=",((int(t/10) * int(t/10))+((t%10)*(t%10))))
print()

#9
Nig = int(input("n => 2 : ")) + 1
a = 0
b = 0
for t in range(1,Nig - 1):
    print(a,"*",t,"+ ",sep="",end=(""))
    b = b + a * t
    a = t
print(a,"*",t + 1,end=(""))
b = b + a * (t + 1)
print("=",b)
print()

#10
Nig = int(input("n => 2 : "))
b = 0
for t in range(1,Nig):
    print(t,"' 2","+",end=(" "))
    b = b + (t*t)
    a = t
print(t + 1,"' 2",end=(""))
b = b + ((t + 1)*(t + 1))
print(" =",b) 
print()

#11
b = 0
for t in range(100,1000,2):
      b = b + t
print(b)
print()

#12
a = int(input("eeeee : "))
for t in range(100,1000):
    if(int(t/100) + int((t/10)%10) + (t%10)== a):
       print(int(t/100),"+",int(t/10)%10,"+",(t%10),"=",int(t/100) + int(t/10)%10 + (t%10))
print()

#13
for t in range(100,1000):
    if((int(t/100) + int((t/10)%10) + (t%10) )% 7 == 0 and t % 7 == 0):
       print(t)
print()

#14
a = int(input("FACTORIAL : ")) + 1
e = 1
for t in range(1,a):
   e = e *t
   print(e)
print()

#15
for t in range(0,10):
   print("20", end =" ")
print()

#16
a = int(input("copy of copy : "))
for t in range(0,a):
   print(a, end =" ")
print()

#17
a = int(input("умножить : "))
b = int(input("на : ")) - 1
r = a
for t in range(0,b):
   a = a + r
print(a)
print()

#18
a = int(input("возвести : "))
b = int(input("в : ")) - 1
r = a
for t in range(0,b):
   a = a * r
print(a)
print()

#19
a = 1
print("время      кол-во клетки")
for t in range(1,26):
   if(t == 1 or t%3==0):
       print(t,"        ",a)
       a = a * 2
print()

#20
a = 10
print("день       дистанция")
for t in range(1,11):
    print(t,"        ",a)
    a = ((a/100)*110)
print()

#21
for t in range(0,20000000):
    t = t
print("3 секунды прошли")
