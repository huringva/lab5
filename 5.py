n= int(input('Введите число: '))
orig = n

count = 0
total = 0
prod = 1
reversed_num = 0

while n>0:
    digit = n%10
    count +=1
    total += digit
    prod *= digit
    reversed_num = reversed_num*10 + digit
    n//=10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {prod}")
print(f"Перевёрнутое число: {reversed_num}")