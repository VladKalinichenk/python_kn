numbers = []
numbers2 = []
n = input("Введить і натисніть Еnter щоб продовжити:")
l = len(n)
i = 0
while i < l:
    n_int = ''
    a = n[i]
    while '0' <= a <= '9':
        n_int += a
        i += 1
        if i < l:
            a = n[i]
        else:
            break
    i += 1
    if n_int != '':
        numbers.append(int(n_int))
print("Числа:",numbers)
largest_number = max(numbers)
print("Максимальне число=",largest_number)
for i in range(len(numbers)):
    if numbers[i] != largest_number:
        numbers2.append(numbers[i]**i)
print("Числа масиву, які піднесені до індексу:",numbers2)
for d in '1234567890':
    n=n.replace(d, '')
n.strip(' ')
while n.find('  ') != -1:
    n = n.replace('  ', ' ')
print("Літери:",n)
def big(n):
 d=""
 h=0
 spl=str(n).split()
 for i in spl:
    for i in spl[h].split():
        a=''.join(spl[h])
        if len(a)==1:
                d=d+a[0].upper()+' '
        else:
                d=d+a[0].upper()+a[1:-1]+a[-1].upper()+' '
        h=h+1
 return d
print("Кожне слово починається і закінчується великою літерою:",big(n))
