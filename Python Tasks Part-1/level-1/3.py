def multiplication_table(x, y):
    for i in range(1, x+1):
        for j in range(1, y+1):
            print(f"{i} * {j} = {i*j}")
        print()


multiplication_table(3, 10)