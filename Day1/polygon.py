class Polygon:

    def __init__(self):
        self.list_of_points = []

    def addPoint(self, x, y):
        self.list_of_points.append([x, y])

    def area(self):
        points = self.list_of_points
        x = 0
        answer = 0
        points.append(points[0])
        while x < len(points) - 1:
            answer1 = points[x][0]*points[x+1][1] - points[x+1][0]*points[x][1]
            x += 1
            answer += answer1
        return abs(answer)/2

    def distance(self, x1, y1, x2, y2):
        return((x1-x2)**2 + (y1 - y2)**2)**(1/2)

    def perimeter(self):
        print(self.list_of_points)
        perimeter = 0
        i = 1
        # for i in range(len(self.list_of_points)-1):
        while (i < len(self.list_of_points)-1):
            x1 = self.list_of_points[i][0]
            x2 = self.list_of_points[i-1][0]
            y1 = self.list_of_points[i][1]
            y2 = self.list_of_points[i-1][1]
            i += 1
            perimeter = (perimeter + (((x1-x2)**2 + (y1 - y2)**2) ** (1/2)) * 2)
        return perimeter/2


inpt1 = input("Enter the first x value. Ex: 4. ")
inpt11 = input("Enter the first y value. Ex: 9. ")
inpt2 = input("Enter the second x value. Ex: 4. ")
inpt22 = input("Enter the second y value. Ex: 4. ")
inpt3 = input("Enter the third x value. Ex: 9. ")
inpt33 = input("Enter the third y value. Ex: 4. ")


large_brown = Polygon()
large_brown.addPoint(int(inpt1), int(inpt11))
large_brown.addPoint(int(inpt2), int(inpt22))
large_brown.addPoint(int(inpt3), int(inpt33))
large_brown.perimeter()
large_brown.area()
print(large_brown.area())
print(large_brown.perimeter())
