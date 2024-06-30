# Crie um programa que receba 10 números inteiros dados pelo usuário e,
# ao final, exiba apenas o maior valor lido e a sua posição. Utilize uma lista.

def posicao_maior(L):
    m = 0
    for i in range(1, len(L)):
        if L[i] > L[m]:
            m = i
    return m

L = []
for i in range(10):
    n = int(input(f'{i+1}º) número? '))
    L.append(n)

posicao = posicao_maior(L)
maior = L[posicao]

print(f'Posicao = {posicao}')
print(f'Maior = {maior}')

