def find_odd(x):
    if (x % 2 != 0):
        return x

nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)