import time


tic = time.time()


def insertion_sorting():
    lst = []
    while True:
        user_input = input("Input number: ")
        lst.append(user_input)
        if user_input == "Stop":
            break
    if len(lst) <= 1:
        return lst

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    lst.remove("Stop")
    return lst


print(insertion_sorting())

toc = time.time()
print(str(toc-tic) + " milliseconds elapsed for this operation.")