def select_two_even_numbers(numbers):
    # Filter out odd numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # Sort the list
    even_numbers.sort()

    # Return the last two elements
    return even_numbers[-2:]

print(select_two_even_numbers)