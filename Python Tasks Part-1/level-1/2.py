def divided_by(x, y):
    for i in range(1, 101):
        if i % x == 0 and i % y == 0:
            print(i, end=' ')


divided_by(3, 5)