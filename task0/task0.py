from random import randint
a = [randint(-100,100) for i in range(30)]
print("Випадкові 30 чисел від -100 до 100:")
print(a)
MaxNum = a[0]
Position = 0
for i in range(1, len(a)):
 if a[i] > MaxNum:
  MaxNum = a[i]
  Position = i+1
print("Максимальниий елемент масиву:", MaxNum, "\nПозиція максимального елемента масиву:", Position)
print("Від’ємні числа утворюють пару:")
for i in range(len(a)-1):
 print(a[i],a[i+1])if a[i]<0 and a[i+1]<0 else None
