s = 0
while True:
    try:
        n = int(input('n? '))
        s += n
    except:
        break
print('Soma =', s)
