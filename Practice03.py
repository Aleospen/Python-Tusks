import math
#1
a = int(input("Введите число а "))
b = int(input("Введите число b "))
answer = min(a, b)
answerSecundus = max(a, b)
print(answer, "= Максимальное", answerSecundus, "= Минимальное")

#2
m = int(input("Введите число m "))
n = int(input("Введите число n "))
if n % m == 0:
  print("n = Делитель")
else:
  print("Нет не делитель")
 
#3
cord = int(input("Введите координаты точки "))
if cord >4:
  print("Точка во второй областей")
elif cord <4:
    print("Точка в первой зоне")
else:
    print("Точка на границе областей")

#4
x = int(input("число x : "))
if(x>0):
        print(math.sin(x) * math.sin(x))
else:
        print(1 - math.sin(x*x))
print()

#5
R = int(input("Радиус круга : "))
n = int(input("Сторона квадрата : "))
if(R * R * 3.14 > n * n):
	print("Круг больше квадрата")
elif(R * R * 3.14 < n * n):
	print("Квадрат больше круга")
else:
	print("Круг и квадрат равны")



#6
numb6 = int(input("Введите целое число "))
afterN = numb6 + 2
if (numb6 % 2 == 0):
  print("Следующее четное после ", numb6, " это ", afterN )

#7
n7 = int(input("Введите натуральное число: "))
if n7>9 & n7 < 100:
    print("Число", n7, " двузначное")
else:
  print("Число не двузначное")


#8
integer = int(input("Введите число на проверку делимости "))
integer2 = int(input("Введите второе число на проверку делимости "))
if integer % integer2 == 0:
    print("Есть делитель")
elif integer2 % integer == 0:
    print("Есть делитель")
else:
    print("Нету делителя")

#9
coordOfPoint1, coordOfPoint1_2 = [int(i) for i in input("Введите две координаты точки :").split()]
if coordOfPoint1 > 2 and coordOfPoint1_2 > 3:
    print("Точка в первой области")
else:
    print("Точка вне первой области")

#11
j = int(input("Введите сторону треугольника: "))
y = int(input("Введите сторону треугольника: "))
u = int(input("Введите сторону треугольника: "))
if j==y==u:
     print("Треугольник равностороний")
else:
     print("Треугольник равнобедренный")

#12
beast = int(input("Введите число на проверку содержания 6 "))
geg = str(beast)
if (geg.__contains__("6")):
    print("Число содержит 6")
else:
    print("6 нету")

#13
print("Введите размеры конверта, в мм.: ")
aboba = int(input("a = "))
boba = int(input("b = "))
print("Введите размеры открытки, в мм.:")
c = int(input("c ="))
d = int(input("d ="))
if aboba and boba >= c and d:
    print("Открытка помещается в конверт")
else:
    print("Открытка не помещается в конверт ")


#14

a = int(input("число : "))
c = 0
if(a%3 == 0):
        c = c + int(a/1000)
        c = c + int((a/100) % 10)
        c = c + int((a /10)%10)
        c = c + int(a%10)
else:
        c = c * int(a/1000)
        c = c * int((a/100) % 10)
        c = c * int((a /10)%10)
        c = c * int(a%10)
print(c)








