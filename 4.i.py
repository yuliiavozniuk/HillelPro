def merge_dictionaries():
    dict_1 = eval(input('Enter your dictionary (example: {"a": 4, "b": 6}) '))
    dict_2 = eval(input('Enter one more dictionary (example: {"c": 8, "d": 10}) '))
    if isinstance(dict_1, dict) and isinstance(dict_2, dict):
        merged = {**dict_1, **dict_2}
        print('Merged dictionary', merged)
    else:
        print('Error')


merge_dictionaries()
