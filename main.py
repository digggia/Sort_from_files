
from pathlib import Path
from os import listdir
import os


path = Path('files')
result_name = 'result.txt'

def read_file(path_files, result_file_name):
    my_os = os.getcwd()
    dicto = {}

    result_path = os.path.join(my_os, path, result_name)

    for item in listdir(path):
        full_path = os.path.join(my_os, path, item)

        with open(full_path, 'rt', encoding='utf-8') as file:
            res = file.readlines()
        dicto[item]= len(res)

    new_sorted_dict = {}
    sorted_values = sorted(dicto.values())

    for i in sorted_values:
        for j in dicto.keys():
            if dicto[j] == i and j != result_name:
                new_sorted_dict[j] = dicto[j]
                break

    with open(result_path, 'wt'):
        pass

    for item in new_sorted_dict:
        full_path = os.path.join(my_os, path, item)

        with open(full_path, 'rt', encoding='utf-8') as read_file, open(result_path, 'a', encoding='utf-8') as write_file:
            line1 = read_file.readlines()
            write_file.write(item)
            write_file.write('\n')
            write_file.write(str(new_sorted_dict[item]))
            write_file.write('\n')
            write_file.writelines(line1)
            write_file.write('\n')


    return ''


read_file(path, result_name)


