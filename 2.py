n = int(input('Введите N:'))
sum = 0
prod = 1
sum_sq = 0

for i in range(1,n+1):
    sum += i
    prod *=i
    sum_sq += i**2

print(f'Сумма:{sum}')
print(f'Произведение:{prod}')
print(f'Сумма квадратов:{sum_sq}')