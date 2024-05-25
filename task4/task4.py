import sys, random

def print_error(error):
    if error == 1:
        print('Не указан путь к файлу')
    elif error == 2:
        print('Необходимо указать лишь путь к файлу!')
    elif error == 3:
        print('Не удалось открыть файл!')
    elif error == 4:
        print('Файл поврежден!')
    elif error == 5:
        print('В файле должно быть хотя бы два отличающихся друг от друга числа!')

def open_file():
	if len(sys.argv) < 2:
		return print_error(1)
	if len(sys.argv) > 2:
		return print_error(2)
	try:
		file = open(sys.argv[1], 'r')
	except:
		return print_error(3)
	else:
		return file

def get_numbers_collection(file):
	lines = file.readlines()
	file.close()
	if len(lines) < 2:
		return print_error(4)
	try:
		numbers_collection = [int(line) for line in lines]
	except:
		return print_error(4)
	else:
		if numbers_collection[0] * len(numbers_collection) == sum(numbers_collection):
			return print_error(5)
		return numbers_collection

def quick_select(numbers_collection, middle_index = None):
    if middle_index is None:
        middle_index = len(numbers_collection) // 2
    pivot_number = numbers_collection[random.randint(0, len(numbers_collection) - 1)]
    lesser_collection, equal_collection, greater_collection = [], [], []
    for number in numbers_collection:
        if number < pivot_number:
            lesser_collection.append(number)
        elif number > pivot_number:
            greater_collection.append(number)
        else:
            equal_collection.append(number)
    if middle_index >= len(lesser_collection) + len((equal_collection)):
    	return quick_select(greater_collection, middle_index - (len(lesser_collection) + len(equal_collection)))	
    elif middle_index < len(lesser_collection):
    	return quick_select(lesser_collection, middle_index)
    else:
    	return pivot_number

def calculate_minimum_moves_quantity(numbers_collection, middle_number):
	minimum_moves_quantity = sum([abs(middle_number - number) for number in numbers_collection])
	print(minimum_moves_quantity)

file = open_file()
if file is not None:
	numbers_collection = get_numbers_collection(file)
	if numbers_collection is not None:
		middle_number = quick_select(numbers_collection)
		calculate_minimum_moves_quantity(numbers_collection, middle_number)