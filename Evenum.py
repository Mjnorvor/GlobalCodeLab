from operator import not_
def is_even(number):
    if number % 2 == 0:
        return True

numbers = [1,56,234,87,4,76,24,69,90,135]
one = list(filter((is_even), numbers))
print(one)
    