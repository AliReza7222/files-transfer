import threading
import os
import sys
import re
import time


if len(sys.argv) < 2:
    sys.exit('Not Enter Address!!!')

address_files = sys.argv[1]
destination_transfer = sys.argv[2]
name_file_run = sys.argv[0]
files = dict()
formats_files_year = dict()


def create_new_directory(dir_name, path='.'):
    address_new_directory = os.path.join(path, dir_name)
    exists = os.path.exists(address_new_directory)

    if not exists:
        os.mkdir(address_new_directory)
        return 1
    else:
        return 0


def return_byte_file(ads_file):
    with open(ads_file, 'rb') as file:
        byt_file = file.read()
    return byt_file


def cpy_file(byte_file, dst_file):
    with open(dst_file, 'wb') as file:
        file.write(byte_file)


def transfer_files(path, list_files):
    formats = ['.pdf', '.docx', '.jpg', '.png']

    for file in list_files:
        format_file = re.findall('\.\w+$', file)

        if len(format_file) == 1 and format_file[0] in formats:
            full_path_file = os.path.join(path, file)
            time_year_file = time.ctime(os.path.getctime(full_path_file)).split(' ')[-1]

            if time_year_file in files and time_year_file in formats_files_year:
                name_format = re.findall('\w+$', format_file[0])[0].capitalize()
                files[time_year_file].append([full_path_file, name_format])

                if name_format not in formats_files_year[time_year_file]:
                    formats_files_year[time_year_file].append(name_format)

            elif time_year_file not in files and time_year_file not in formats_files_year:
                files[time_year_file] = []
                formats_files_year[time_year_file] = []

                name_format = re.findall('\w+$', format_file[0])[0].capitalize()

                formats_files_year[time_year_file].append(name_format)
                files[time_year_file].append([full_path_file, name_format])


create_new_directory("File_Transfer", path=destination_transfer)

for item in list(os.walk(address_files)):
    threading.Thread(target=transfer_files(item[0], item[-1])).start()

for year_file, list_formats in formats_files_year.items():
    create_new_directory(year_file, f'{destination_transfer}\\File_Transfer')
    for format_file in list_formats:
        create_new_directory(format_file, f'{destination_transfer}\\File_Transfer\\{year_file}')

for year, address in files.items():
    for address_file in address:
        src_address = address_file[0]
        name_file = os.path.basename(src_address)
        dst_address = os.path.join(f'{destination_transfer}\\File_Transfer\\{year}\\', f'{address_file[-1]}\\{name_file}')
        byte_file = return_byte_file(src_address)
        cpy_file(byte_file, dst_address)
        print(f"{src_address}   Done ! ")

print('\n************  Complete !!!  ************\n')
