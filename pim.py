n = int(input())

print(1, end='')
for i in range(2, n+1):
    if i % 4 == 0:
        print(' pim', end='')
    else:
        print(f' {i}', end='')
