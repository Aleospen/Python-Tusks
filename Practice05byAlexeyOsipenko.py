'''
#1
n = 5
FGC = 0
while FGC >= n:
   print (FGC+=1)
'''
#2
exodus = 9
while exodus != 101:
    exodus+=1
    if exodus %2 == 0:
        print(exodus, end =' ')     

 #6
e = 0.5
while e >= 13.5:  
    e+=0.5 
    print(e + 0.5, end =' ')

    

#3
print("Фунты        Киллограммы")
for i in range(1, 11):
    print(i, "          ", 0.453*i )


#4
for t in range(1, 8):
    print( t, "* 7=", t*7)

#5
for d in range(10, 100):
    print(d%2!==0)

#6
for r in range(10, 99):
    print(r=3 or 7 if r%2!=0 else "False")

#9      
n = int(input("Введите значение n "))
answer_9 = sum(i*(i+1) for i in range(n))
print(f"{1*2}+{2}+{2*3}+{(n-1)*{n}}={answer_9}")



#11
answer_11 = 0; 
for i in range(100, 1000):
    if i%2==0:
        answer_11+=i
print(answer_11)


#15
print (" 20 " * 10 )

#19
print("время        Кол-во клеток")
for q in range(1, 10):
    print(q+2, "      ", q**2  )
    
#20

print("Time       Distance")
cr = 10
for c in range(1, 10):
    print(c, c + (c/100*10))


