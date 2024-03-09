add_ten = lambda x: x + 10
print(add_ten(10))

multiply = lambda x,y : x * y
print(multiply(2,5))

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)