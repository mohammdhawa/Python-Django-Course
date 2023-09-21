def divisable_by_y(x, y):
    if x < 0 or x > 100:
        print("x must be between 0 and 100")
        return
    try:
        for i in range(x, 101):
            if i % y == 0:
                print(f"{i} id divisable by {y}")
    except ZeroDivisionError:
        print("Y shouldn't be 0")


divisable_by_y(9, 21)
