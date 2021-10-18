from math import sqrt


def load_point_from_file(file_path):
    f = open(file_path, "r")
    line = f.readline()
    points = list(map(lambda p: p.split(), line.split(',')))
    return points


def get_square(points):
    if len(points) != 3 and len(points[0]) != 2:
        print("Passed array is not triangle")
        return

    sides = __get_sides__(points)
    half_perimeter = sum(sides) / 2
    square = sqrt(half_perimeter *
                  (half_perimeter - sides[0]) *
                  (half_perimeter - sides[1]) *
                  (half_perimeter - sides[2]))

    return square


def __get_sides__(points):
    sides = []
    for i in range(3):
        x1 = int(points[i][0])
        y1 = int(points[i][1])
        x2 = int(points[i-1][0])
        y2 = int(points[i-1][1])

        side = sqrt((x2-x1)**2 + (y2-y1)**2)
        sides.append(side)

    return sides
