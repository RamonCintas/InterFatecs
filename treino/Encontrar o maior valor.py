# Crie um programa que receba 10 números inteiros dados pelo usuário e,
# ao final, exiba apenas o maior valor. Utilize uma lista.

def maior_valor(L):
    m = L[0]
    for i in range(1, len(L)):
        if L[i] > m:
            m = L[i]
    return m

L = []
for i in range(10):
    n = int(input(f'{i+1}º) número? '))
    L.append(n)

print(f'Maior = {maior_valor(L)}')
