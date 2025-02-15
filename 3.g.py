def common_elements():
    list_1 = input('Enter space-separated list of numbers: ').split()
    list_2 = input('Enter one more space-separated list of numbers: ').split()

    list_1 = [int(num) for num in list_1]
    list_2 = [int(num) for num in list_2]

    common = list(set(list_1) & set(list_2))
    print(f"Спільні елементи: {common}")


common_elements()