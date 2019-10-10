def SelectionSort():

    list = [3, 4, 1, 2, 5]

    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]
    return print(list)


SelectionSort()
