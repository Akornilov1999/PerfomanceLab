import sys

def print_error(error):
	if error == 1:
		print('Не указаны размер кругового массива и/или интервал длины')
	elif error == 2:
		print('Необходимо указать лишь размер кругового массива и интервал длины')
	elif error == 3:
		print('Размер массива и интервал длины должны представлять собой натуральные числа и быть отличными от единиц!')

def get_data():
	if len(sys.argv) < 3:
		return print_error(1)
	if len(sys.argv) > 3:
		return print_error(2)
	try:
		number, interval = int(sys.argv[1]), int(sys.argv[2])
	except:
		print_error(3)
	else:
		if number < 2 or interval < 2:
			return print_error(3)
		return (number, interval)

def determine_path(number, interval):
	current_number = 1
	print(1, end='')
	while True:
		for _ in range(interval - 1):
			current_number = 1 if current_number == number else current_number + 1
		if current_number == 1:
			break
		print(current_number, end='')

data = get_data()
if data is not None:
	determine_path(*data)