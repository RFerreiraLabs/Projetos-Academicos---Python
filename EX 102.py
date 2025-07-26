def fatorial(n,show):
    if show == False:
        f = 1
        for n in range(n, 0, -1):
            f *= n
        return f

    else:
        f = 1
        for n in range(n, 0, -1):
            print(f'{n} x ', end = '')
            f *= n
        return f



# PROGRAMA PRINCIPAL:

print(fatorial(5,True))
print(fatorial(5, False))
