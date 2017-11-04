# Программа считывает массив чисел из строки
# и выписывает в обратном порядке числа в четных позяциях.
s=[]
a=int(input()).split(' ')
for i in range (a):
    if i%2==1:
        s.append(a[i])
print(' '.join(reversed(s)))
