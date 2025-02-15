def some_keys():
    dictionary = {}
    number = int(input('Number of pairs: '))

    for _ in range(number):
        key = input('Enter key: ')
        value = input('Enter value: ')
        dictionary[key] = value

    print('Keys:', list(dictionary.keys()))


some_keys()