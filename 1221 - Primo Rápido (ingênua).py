from benchmark import tempo

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
for _ in range(n):
    x = int(input())
    if primo(x):
        print('Prime')
    else:
        print('Not Prime')
