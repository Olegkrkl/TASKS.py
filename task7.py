def print_even_numbers(n, m):
    start = -n if -n % 2 == 0 else -n + 1

    for num in range(start, n + 1, m):
        if num % 2 == 0:
            print(num)
m = 3

n = 20
print("Парні числа від -{} до {} з кроком {}: ".format(n, n, m))
print_even_numbers(n, m)