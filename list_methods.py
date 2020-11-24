numbers = [5, 2, 4, 3, 8, 5, 6, 5]

numbers.append(20)
numbers.insert(2, 40)
print(numbers)
numbers.remove(40)
print(numbers)
print(numbers.index(8))


# Exercice

numbers = list(dict.fromkeys(numbers))

print(numbers)