def newton(n, k):
    gora = 1
    dol = 1
    for i in range(k):
        gora *= n - i
        dol *= i + 1
    return gora // dol


print(newton(7, 2))

