def merge_dicts():
    def input_dict():
        dictionary = {}
        n = int(input('Enter number of pairs: '))
        for _ in range(n):
            key = input('Enter key: ')
            value = input('Enter value: ')
            dictionary[key] = value
        return dict(dictionary)

    print('First dictionary: ')
    dict1 = input_dict()

    print('Second dictionary: ')
    dict2 = input_dict()

    merged = {**dict1, **dict2}
    print('Merged dictionary', merged)


merge_dicts()