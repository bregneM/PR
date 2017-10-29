#Программа вычисляет min,max и среднее значение элементов массива, введенное с консоли.
a=[]
n=int(input())
avr=min=max=sum=0
for i in range(n):
	a.append(int(input()))
	if(a[i]<min):
		min=a[i]
	if(a[i]>max):
		max=a[i]
	sum+=a[i]
avr=sum//len(a)
print ("avr=",avr,"min=",min,"max=",max)
