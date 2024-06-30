def primo(n: int) -> bool:
    qtd_divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd_divisores += 1
    if qtd_divisores == 2:
        return True
    else:
        return False

n = int(input())

encontrei = False
p2 = n
while encontrei == False: # (p1, p2)
    if primo(p2) and primo(p2-2):
        encontrei = True
    else:
        p2 -= 1
print(p2-2, p2)
        
