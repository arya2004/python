def remove_duplicates(number):
    for numbers in number:
        if number.count(numbers) >= 2:
            number.remove(numbers)
            number.sort()
            return number


print(remove_duplicates([1, 5, 3, 4, 5, 6, 3]))
