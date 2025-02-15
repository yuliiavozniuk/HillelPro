def merge_sets():
    def input_set():
        some_set = set()
        number_of_elements = int(input('Enter number of elements: '))
        for _ in range(number_of_elements):
            some_set.add(input('Enter element: '))
        return some_set

    print('First set: ')
    set1 = input_set()

    print('Second set: ')
    set2 = input_set()

    print('Merged set', set1 | set2)


merge_sets()