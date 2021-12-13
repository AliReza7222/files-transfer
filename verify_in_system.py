# b_kh
# ali_coder

import os
import time
import sys
import re

# distination and script file
list_d_s = sys.argv
"----------------------------"
dict_file = dict()
file_s = list(os.walk(list_d_s[1]))
format_photos = ['.jpg', '.jpeg', '.png']
format_videos = ['.mp4', '.avi', '.3gp', '.mpeg', '.mkv', '.wmv', '.mov']
# sent files
if not(os.path.isdir(list_d_s[2])):
    os.mkdir(list_d_s[2])
# division file photos and videos
for file in file_s:
    for file_p_or_vd in file[2]:
        # calculatour year for each file
        year = time.ctime(os.path.getmtime(os.path.join(file[0], file_p_or_vd))).split()[-1]
        regex_file = re.findall('(\.\w+)$', file_p_or_vd.lower())
        if len(regex_file) > 0 and regex_file[0] in format_photos:
            address = os.path.join(file[0], file_p_or_vd)
            if year not in dict_file:
                dict_file[year] = [['p', address, file_p_or_vd]]
            elif year in dict_file:
                dict_file[year].append(['p', address, file_p_or_vd])
        elif len(regex_file) > 0 and regex_file[0] in format_videos:
            address = os.path.join(file[0], file_p_or_vd)
            if year not in dict_file:
                dict_file[year] = [['v', address, file_p_or_vd]]
            elif year in dict_file:
                dict_file[year].append(['v', address, file_p_or_vd])
# found files for each year
for year_file in list(dict_file.keys()):
    if not (os.path.isdir(os.path.join(list_d_s[2], year_file))):
        os.mkdir(os.path.join(list_d_s[2], year_file))
    for file_format in dict_file[year_file]:
        with open(file_format[1], 'rb') as copy_file:
            copy_byte = copy_file.read()
            if file_format[0] == 'p':
                if not (os.path.isdir(os.path.join(list_d_s[2], year_file, 'photos'))):
                    os.mkdir(os.path.join(list_d_s[2], year_file, 'photos'))
                with open(os.path.join(list_d_s[2], year_file, 'photos', file_format[-1]), 'wb') as write_file:
                    copy = write_file.write(copy_byte)
                    print(f"get file : {os.path.join(list_d_s[2],year_file,'photos',file_format[-1])}")
            elif file_format[0] == 'v':
                if not (os.path.isdir(os.path.join(list_d_s[2], year_file, 'videos'))):
                    os.mkdir(os.path.join(list_d_s[2], year_file, 'videos'))
                with open(os.path.join(list_d_s[2], year_file, 'videos', file_format[-1]), 'wb') as write_file:
                    copy = write_file.write(copy_byte)
                    print(f"get file : {os.path.join(list_d_s[2], year_file, 'videos', file_format[-1])}")
    # remove file absord
    found_list_absord = os.listdir(os.path.join(list_d_s[2], year_file))
    if len(found_list_absord) == 0:
        os.rmdir(os.path.join(list_d_s[2], year_file))
