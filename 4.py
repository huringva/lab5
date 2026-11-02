n = int(input('Введите число: '))
original = n
fact = []

div = 2
while div*div<=n:
    while n%div==0:
        fact.append(div)
        n//=div
    div += 1

if n>1:
    fact.append(n)

print(f"{ original } = {' x '.join(map(str , fact))}")

