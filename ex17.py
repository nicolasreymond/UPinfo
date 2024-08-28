def table_of_n(n):
    print(f"Table of {n}")
    for i in range(1, 11, 1):
        val = n * i
        print(f'{n} * {i:2d} = {val:2d}')
    print("")

for n in range(1, 11):
    table_of_n(n)