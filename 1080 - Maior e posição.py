def posicao_maior(L):
    m = 0
    for i in range(1, len(L)):
        if L[i] > L[m]:
            m = i
    return m

L = []
for i in range(100):
    n = int(input())
    L.append(n)

posicao = posicao_maior(L)
maior = L[posicao]

print(maior)
print(posicao+1)

