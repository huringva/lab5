n = int(input('Введите число: '))
o = n
rev = 0

temp = n
while temp>0:
    digit = temp%10
    rev = rev * 10 + digit
    temp //=10

if o == rev:
    print(f"{o} - палиндром")
else: print(f"{o} - не палиндром")