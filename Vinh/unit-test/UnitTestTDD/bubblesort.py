
def bubblesort(list, dec = 0):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                dec += 1
    if dec:
        list.reverse()
    return list