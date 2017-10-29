#Программа создает массив заполненный первыми N простыми числами. (подсказка решето Эратосфена)
n=int(input())
a=[True]*n
for i in range(2, n):
	for b in range(i*2, n,i):
		a[b] = False
a=[i for i in range(2, n) if a[i]]
a=a[0:n]
print(a)