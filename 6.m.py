def even_list():
    numbers = []
    number_of_digits = int(input('Enter number of digits: '))
    for _ in range(number_of_digits):
        num = int(input('Enter your number: '))
        numbers.append(num)

    even_numbers = [num for num in numbers if num % 2 == 0]
    print('The list of even numbers:', even_numbers)


even_list()