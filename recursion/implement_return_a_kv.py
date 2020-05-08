def myfn(x, n):
    if x <= n:
        print('Invalid inputs')
        return None, None
    for i in range(x):
        a = i
        b = i + 1
        if i == n:
            return (a, b)


m, n = myfn(5, 6)
print(f'{m} {n}')


kv = myfn(5, 3)
print(f'{kv}')

a, b = myfn(5, 3)
print(f'{a}, {b}')

# (*), b = myfn(5, 3)
# print(f'{b}')
