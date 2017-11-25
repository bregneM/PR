#Программа ищет количество сочетаний
n=int(input())
p=[(i, j) for i in range(1, n) for j in range(i+1, n+1)]
print(len(p))