'''════════════════════════════════════════════════════════════════════════════╗
╠══════════════════════════════════════════════════════════════════════════════╣
║ Competição    :  InterFatecs 2018 - 2ª fase                                  ║
║ Programa      :  Problema B - Fliperama                                      ║
║ Linguagem     :  Python 3                                                    ║
║ Compilador    :  CPython (3.10.2)                                            ║
║ Versão        :  A (Rev. 1)                                                  ║
╚════════════════════════════════════════════════════════════════════════════'''

def maximo_m(f, l, c, memo={}):
    if c == len(f[l])-1: return f[l][c]
    if (l,c) not in memo:
        memo[(l,c)] = f[l][c] + max(maximo_m(f, l+1, c), maximo_m(f, l, c+1))
    return memo[(l,c)]

def minimo_m(f, l, c, memo={}):
    if c == len(f[l])-1: return f[l][c]
    if (l,c) not in memo:
        memo[(l,c)] = f[l][c] + min(minimo_m(f, l+1, c), minimo_m(f, l, c+1))
    return memo[(l,c)]

n = int(input())
flip = []
for i in range(n):
    linha = input().split()
    linha = [int(x) for x in linha]
    flip.append(linha)
print('maximo:', maximo_m(flip, 0, 0))
print('minimo:', minimo_m(flip, 0, 0))
