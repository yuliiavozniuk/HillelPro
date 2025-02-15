def average_numbers():
    numbers = input('Enter space-separated numbers: ').split()
    numbers = [float(num) for num in numbers]
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f'Average is: {average}')
    else:
        print('The list is empty.')

average_numbers()