def ha_digito(digito, n):
    while n > 0:
        dmd = n % 10
        if dmd == digito:
            return True
        n = n // 10
    return False

def sem_repeticao(n):
    while n >= 10:
        dmd = n % 10
        n = n // 10
        if ha_digito(dmd, n):
            return False
    return True

while True:
    try:
        n, m = input().split()
        n, m = int(n), int(m)
        qtd = 0
        for i in range(n, m+1):
            if sem_repeticao(i):
                qtd += 1
        print(qtd)
    except:
        break
