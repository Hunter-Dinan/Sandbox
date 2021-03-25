def main():
    numbers = [3, 5, 90, -1, 23, -123]
    display_positive_negative_numbers(numbers)


def display_positive_negative_numbers(numbers):
    positive_numbers = []
    negative_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)
    print("Positive numbers: {}".format(positive_numbers))
    print("Negative numbers: {}".format(negative_numbers))

    # Use list comprehensions instead of separate for loop
    positive_numbers = [number for number in numbers if number > 0]
    print(positive_numbers)


main()
