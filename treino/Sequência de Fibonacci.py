n = int(input('n? '))
t1 = 1
t2 = 1
ta = t1
for i in range(3, n+1):
    ta = t1 + t2
    t1 = t2
    t2 = ta
print(ta)
