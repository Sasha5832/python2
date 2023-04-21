def iloczyn(*num, n=2):
    odp = 1
    for x in num:
        odp = odp * x**n
    print(odp)


iloczyn(1, 2, 3, 4, 5)
