def odd_even_lists(x, y):
    odd = [num for num in range(x, y+1) if num % 2]
    even = [num for num in range(x, y+1) if num % 2==0]

    print(f"Odd list: {odd}")
    print(f"Even list: {even}")


odd_even_lists(5, 23)