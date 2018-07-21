'''
Created on Sept 24, 2017

@author: YOUR NAME HERE
'''

filename = "athletes.txt.py"


def average_height(line):
    x = 0
    for i in line:
        x += int(i)
    return x / len(line)


def height_range(line):
    maximum = 0
    for num in line:
        if str(num) > str(maximum):
            maximum = num
        minimum = line[0]
        if num < minimum:
            minimum = num
    return[minimum, maximum]


def height_between(line):
    height1 = 72
    height2 = 78
    answer = 0
    for num in line:
        if height1 <= int(num) <= height2:
            answer += 1
        else:
            continue
    print(answer)



def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        answer.append(line[:-1].split(':'))
    return answer


if __name__ == '__main__':
    data = process(filename)
    print("The data is:")
    answer = []
    for item in data:
        answer.append(item[4])
        print(item)
    print("The average height is " + str(average_height(answer)))
    print("The range of heights is " + str(height_range(answer)))
    print("The amount of people who are between six feet and six feet six inches is " + str(height_between(answer)))

    # 1)The variable file_name is assigned to the file athletes.txt.py in the beginning of the program.
    # 2)The function process returns a list of strings.
    # 3)The function process returns a list of strings after clearing whitespace before and after words in the file.
    # 4)
