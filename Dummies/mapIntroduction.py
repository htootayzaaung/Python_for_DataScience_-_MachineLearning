def square(n):
    return n ** 2

squares = map(square, range(1, 10, 2))

print(list(squares))