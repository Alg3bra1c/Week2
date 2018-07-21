'''
Created on Sep 17, 2017

@author: YOUR NAME HERE
'''


def process(name):
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        answer.append(line)
    return answer


print(process(name))


if __name__ == '__main__':
    filename = "grades.txt"
    data = process(filename)
    for each in data:
        print
        each
    print
    # print "Average grade is ", classAverage(data)
    # print "Maximum grade is ", maxGrade(data)
    grade1 = 80
    grade2 = 90
    # print "Names of people with grades between ", grade1, " and ", grade2, " inclusive"
    # names = namesForGrades(data, grade1, grade2)
    # ADD CODE TO PRINT the names one per line
    print
    year1 = 1995
    year2 = 1997
    print
    "Number born from ", year1, "to", year2, "is",
    # print howManyInRange(data, year1, year2)

#  3)String
#  4)It appends the words in line without the leading or trailing whitespace into answer and returns answer.
#  5)
