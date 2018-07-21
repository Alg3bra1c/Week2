import time


def searching(a, input):
    for index in range(len(a)):
        if input == a[index]:
            return index

    return -1


start = time.time()


(searching(range(0, 20001), 20000))

end = time.time()

print(end-start)


def search():
    lst = (range(0, 20001))
    x = input("Which number would you like to find?")
    if x in lst:
        print("Success")
    else:
        return "Failure"
		

search()

