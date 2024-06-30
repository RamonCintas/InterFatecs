from random import randint

def gera(n, vmin=10, vmax=99):
    L = []
    for i in range(n):
        L.append(randint(vmin, vmax))
    return L

def troca(L, i, j):
    assert 0 <= i < len(L) and 0 <= j < len(L)
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def empurra(L, n):
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            troca(L, i, i+1)
        i += 1

def bubble_sort(L):
    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1
