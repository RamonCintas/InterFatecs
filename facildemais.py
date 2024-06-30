n = int(input())
qtd = 0

for i in range(1, n+1):
    p = int(input())
    if p > 1:
        qtd += 1

if qtd % 2 == 0:
    print('par')
else:
    print('impar')
