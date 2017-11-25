#Программа обрабатывает файлы с результатами секвенирования.
#В первой строке файла лежит количество цепочек и другая вспомогательная информация.
#В остальных строчках - последовательности нуклеотидов.
#Если файл корректный - нужно вывести в консоль информацию о том, что секвенировалось(DNA/RNA)

#запуталась в генераторе списка, проще было без этого, но очень хочу научиться через него работать.
try:
  f=open("3-in.txt")
  for line in f:
    print(line)
except FileNotFoundError:
  print("Error")

a=[]
G=C=A=T=U=0
f=open("3-in.txt")
F=[f.readlines().pop(0) for line in (F)]
a=[a.append(line), ' '.join(a).upper() for line in (F)]
print(a)
for i in range(len(a)):
	 G=a[i].count('G')
	 C=a[i].count('C')
	 A=a[i].count('A')
	 T=a[i].count('T')
	 U=a[i].count('U')
	 if a[i].count('U'):
	   print('RNA:','U:',U, 'G:', G, 'C:', C)
	 else:
	   print('DNA:', 'A:', A, 'T:', T, 'G:', G, 'C:', C)
