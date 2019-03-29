fileref = open("labdata.txt", "r")

from statistics import mean

def plot_regression():
    yList = []
    n = 5
    for aline in fileref:  # iterate through each line in the file
        values = aline.split()
        x_coordinates = [int(x) for x in values[:1]] #convert strings in x position to int
        y_coordinates = [int(y) for y in values[1:]] #convert strings in y position to int
        print('Coordinates: ', values)
        print('X coordinates: ', x_coordinates)
        print('Y coordinates: ', y_coordinates)

    #y = (mean(y) + )
    m = ((sum(x_coordinates) * sum(y_coordinates)) - n * (mean(x_coordinates) * mean(y_coordinates) / (sum(x_coordinates ** 2) - (n * x_coordinates) ** -2)))

    #print('M:', m)

plot_regression()

