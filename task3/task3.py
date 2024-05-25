import sys, json

def print_error(error):
    if error == 1:
        print('Не указаны пути к одному или нескольким файлам!')
    elif error == 2:
        print('Необходимо указать лишь пути к трем файлам!')
    elif error == 3:
        print('Не удалось открыть первый файл!')
    elif error == 4:
        print('Не удалось открыть второй файл!')
    elif error == 5:
        print('Не удалось открыть третий файл!')

def open_files():
    if len(sys.argv) < 4:
        return print_error(1)
    if len(sys.argv) > 4:
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
                try:
                    file3 = open(sys.argv[3], 'w')
                except:
                    return print_error(5)
                else:
                    return (file1, file2, file3)

def get_data_from_jsons(file1, file2):
    data = json.load(file1)
    tests_collection = data['tests']
    data = json.load(file2)
    values_list = data['values']
    values_collection = {}
    for item in values_list:
        values_collection[item['id']] = item['value']
    return (tests_collection, values_collection)

def decompose(tests_collection, values_collection):
    report_collection = []
    for test in tests_collection:
        if 'value' in test:
            test['value'] = values_collection[test['id']]
        if 'values' in test:
            report_collection.append(decompose(test['values'], values_collection))

def put_data_to_json(report_collection, file3):
    report_collection = {'tests': report_collection}
    json.dump(report_collection, file3)        

def close_files(file1, file2, file3):
    file1.close()
    file2.close()    
    file3.close()

files = open_files()
if files is not None:
    collections = get_data_from_jsons(files[0], files[1])
    if collections is not None:
        decompose(*collections)
        put_data_to_json(collections[0], files[2])
        print('Готово!')