numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers = list(filter((lambda x: x % 2 == 0), numbers))
print(even_numbers)