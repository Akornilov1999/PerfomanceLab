import sys

def print_error(error):
    if error == 1:
        print('Не указаны пути к одному или обоим файлам!')
    elif error == 2:
        print('Необходимо указать лишь пути к обоим файлам!')
    elif error == 3:
        print('Не удалось открыть первый файл!')
    elif error == 4:
        print('Не удалось открыть второй файл!')
    elif error == 5:
        print('Первый файл поврежден!')
    elif error == 6:
        print('Радиус должен являться натуральным числом!')
    elif error == 7:
        print('Второй файл поврежден!')

def open_files():
    if len(sys.argv) < 3:
        return print_error(1)
    if len(sys.argv) > 3:
        return print_error(2)
    else:
        try:
            file1 = open(sys.argv[1], 'r')
        except:
            return print_error(3)
        else:
            try:
                file2 = open(sys.argv[2], 'r')
            except:
                return print_error(4)
            else:
                return (file1, file2)

def get_circe_data(file):
    lines = file.readlines()
    file.close()
    if len(lines) != 2:
        return print_error(5)
    try:
        center = [int(coordinate) for coordinate in lines[0].split()]
    except:
        return print_error(5)
    else:
        if len(center) != 2:
            return print_error(5)
        else:
            try:
                radius = int(lines[1])
            except:
                return print_error(5)
            else:
                if radius < 1:
                    return print_error(6)
                return (*center, radius)

def get_points_collection(file):                  
    lines = file.readlines()
    if len(lines) == 0:
        return print_error(7)
    file.close()
    points_collection = []
    for line in lines:
        try:
            point = [int(point) for point in line.split()]
        except:
            return print_error(7)
        else:
            if len(point) != 2:
                return print_error(7)
            points_collection.append((point[0], point[1]))
    else:
        return points_collection

def determine_location(circle_data, points_collection):
    for point in points_collection:
        difference = (point[0] - circle_data[0])**2 + (point[1] - circle_data[1])**2 - circle_data[2]**2
        if difference > 0:
            print(2)
        elif difference < 0:
            print(1)
        else:
            print(0)

files = open_files()
if files is not None:
    circle_data = get_circe_data(files[0])
    if circle_data is not None:
        points_collection = get_points_collection(files[1])
        if points_collection is not None:
            determine_location(circle_data, points_collection)