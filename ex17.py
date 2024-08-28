for n in range(1, 11):
    print(f"Table of {n}")
    for i in range(1, 11, 1):
        val = n * i
        print(f'{n} * {i:2d} = {val:2d}')
    print("")