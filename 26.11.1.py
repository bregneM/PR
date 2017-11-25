#Чиса Фиббоначи. An=An-1+An-2.
def fib():
  a, b=0, 1
  while True:
    yield a
    a, b=b, a+b

n=int(input())
for f in fib():
  if f>n:
    break
  print(f)