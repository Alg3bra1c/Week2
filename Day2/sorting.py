import time


tic = time.time()


def insertion_sorting(a):
    if len(a) <= 1:
        return a

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


print(insertion_sorting([100, 9, 5, 4, -1, 1, 1, 2, 3, 7]))

toc = time.time()
print(str(toc-tic) + " seconds elapsed for this operation.")
