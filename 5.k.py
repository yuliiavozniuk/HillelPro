def ifis_subset():
    def input_set():
        some_set = set()
        number_of_elements = int(input('Enter number of elements: '))
        for _ in range(number_of_elements):
            some_set.add(input('Enter element: '))
        return some_set

    print('First set: ')
    set_1 = input_set()

    print('Second set: ')
    set_2 = input_set()

    print('Is set a subset?', set_1.issubset(set_2))


ifis_subset()