def merge_sets():
    set_1 = eval(input('Enter your set, example: {1, 2, 3}): '))
    set_2 = eval(input('Enter one more set, example: {3, 4, 5} '))
    if isinstance(set_1, set) and isinstance(set_2, set):
        print('Merged set', set_1 | set_2)
    else:
        print('Error')


merge_sets()