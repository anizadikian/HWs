def bubblesort():

    list = [10, 1, 3, 9, 4, 2]
    for i in range(len(list) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if list[j + 1] < list[j]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swap = False
        if no_swap:
            print(list)
            return list

bubblesort()
