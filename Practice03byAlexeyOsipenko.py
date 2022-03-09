import math
#1
numb1 = int(input("Введите число а "))
numb1_2 = int(input("Введите число b "))
ans1_2 = min(numb1, numb1_2)
ans1 = max(numb1, numb1_2)
print(ans1, "= Максимальное", ans1_2, "= Минимальное")

#2
m = int(input("Введите число m "))
n = int(input("Введите число n "))
if n % m == 0:
  print("n = Делитель")
else:
  print("Нет не делитель")
 
#3
cord = int(input("Введите координаты точки "))
if cord >=8:
  print("Точка вне областей")
elif cord <=4:
    print("Точка в первой зоне")
else:
    print("Точка во второй области")

#4
x = int(input("число x : "))
if(x>0):
        print(math.sin(x) * math.sin(x))
else:
        print(1 - math.sin(x*x))
print()

#5
R = int(input("R круга : "))
n = int(input("сторона квадрата : "))
if(R * R * 3.14 > n * n):
	print("круг больше квадрата")
elif(R * R * 3.14 < n * n):
	print("квадрат больше круга")
else:
	print("они равны")
print()
"""
radOfRoud = int(input("Введите радиус круга "))
sideOfSquare = int(input("Введите сторону квадрата"))
areaOfRound = math.pi * radOfRoud**2 
areaOfSquare = sideOfSquare  * 4
if areaOfRound == areaOfSquare:
    print("Площади равны")
elif areaOfSquare > areaOfRound:
    print("Площадь квадрата больше")
else:
    print("Площадь круга больше")
"""

#6
n6 = 0
if n6%2==0:
    print("Next will be", n6+2)
else:
    n6%2!=0

    print("Следущим будет", n6+1)

#7
n6 = int(input("Введите натуральное число: "))
if n6%2==0:
    print("Число", n6+2)
else:
    print("Next will be", n6+1)

#8
numi8 = 2
numi82 = 6
if numi8%numi82==0:
    print("True")
elif numi82%numi8==0:
    print("True")
else:
    print("Нету делителя")

#9
coordOfPoint1, coordOfPoint1_2 = [int(i) for i in input("Введите две координаты точки :").split()]
if coordOfPoint1 >=2 and coordOfPoint1_2 >=3:
    print("Точка в первой области")
else:
    print("Точка вне первой области")

#11
j = int(input("Введите стороны треугольника:"))
y = int(input("Введите стороны треугольника:"))
u = int(input("Введите стороны треугольника:"))
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
aboba = int(input("a ="))
boba = int(input("b ="))
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

'''
q = int(input("Введите натуральное четырехзначное число: "))
if q/3==0:
     ancbp = q/3
     qw = str(q)
     print(qw, "/ 3 =", ancbp)
else:
 q_22 = q//1000
q_2 = q//100
q_3 = q//10
q_4 = q//1110
ans_14 = q_22+q_2+q_3+q_4
print("Сумма его чисел ", ans_14)
'''






