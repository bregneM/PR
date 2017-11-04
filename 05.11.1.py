#Программа считывает текст состоящий из 1 строки.
#слова с нечетным номером переводит в верхний регистр,с четным в нижний.
word=str(input()).split()
i=0
for i in range (len(word)):
    if i%2==0:
        word[i]=word[i].upper()
    else:
        word[i]=word[i].lower()
word=' '.join(word)
print(word)
