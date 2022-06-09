#1
AgeOfMitya = int(input("Введите возраст Мити "))
AgeOfVasya = int(input("Введите возраст Васи "))
if AgeOfMitya > AgeOfVasya :
    print("Митя старше Васи")
elif AgeOfVasya > AgeOfMitya :
    print("Вася старше Мити")
else:
    print("Вася и Митя ровесники")

#2
WeightOfBoxer = int(input("Введите вес боксёра "))
if WeightOfBoxer < 60:
    print("Боксёр в легкой категории ")
elif WeightOfBoxer < 64:
    print("Боксёр в первой полусредней категории")
elif WeightOfBoxer < 69:
    print("Боксёр в полусредней категории")
else:
    print("Боксёр вне весовой категории")

#3
a = int(input("Введите число a "))
b = int(input("Введите число b "))
if a % b == 0:
    print("a делитель числа b")
elif b % a == 0:
    print("b делитель чиал а")
else:
    print("делителя нет")

#4
DaysOfWeek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
numb = int(input("Введите номер "))
if numb == 1:
    print(DaysOfWeek[0])
if numb == 2:
    print(DaysOfWeek[1])
if numb == 3:
    print(DaysOfWeek[2])
if numb == 4:
    print(DaysOfWeek[3])
if numb == 5:
    print(DaysOfWeek[4])
if numb == 6:
    print(DaysOfWeek[5])
if numb == 7:
    print(DaysOfWeek[6])

#5
Months5 = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
s = int(input("Месяц - "))
print(Months5[s-1])

#6
Months1 = {1, 3, 5, 7, 8, 10, 12}; Months2 = {4, 6, 9, 11}; 

n = int(input("Введите порядковый номер месяца "))

if n in Months1:
    print('31 день')
elif n in Months2:
    print('30 дней')
else:
    print('28 дней')

#7
sec = int(input("Введите время в секундах "))
min = int(input("Введите время в минутах ")) 
#ans = sec if min * 60 < sec else min 
ans1 = print("Секунд больше" if min * 60 < sec else "Время в минутах больше" )

#8
m = int(input("Введите значение m "))
n = int(input("Введите значение n "))
answer_8 = m if m%n==0 else n
print(answer_8)

#9
a = int(input("число a : "))
b = int(input("число b : "))
otvet = ((a+b)/3) if (a%3 == 0 and b%3 == 0) else ((a+b)*3)
print(otvet)




