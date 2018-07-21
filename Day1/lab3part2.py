def all_same():
    value1 = input("Put in a number.")
    value2 = input("Put in a number.")
    value3 = input("Put in a number.")
    if value1 == value2 and value1 == value3:
        print("These numbers are the same.")
        return True
    else:
        print("These numbers are different.")
        return False


all_same()