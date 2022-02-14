from importlib.resources import path
import os
import re
import sys

list = []
PATH = './toChange/'
'''invalide characters list: <>:"/\|?*'''
reg_ex = r'[<>:"/\\|?*]'
error = 0

'''
Get all directories, subdirectories and files in the toChange directory to list
'''
for root, dirs, files in os.walk(PATH):
    list.append([root, dirs, files])

'''
loop through the list, from the end to the first
'''
length = len(list)
for i in range(0, length):
    level = list[length-(i+1)]
    root = level[0]
    dirs = level[1]
    files = level[2]
    print(root, dirs, files)
    
    if root != PATH:
        root_path = root + "/"
    else:
        root_path = root

    for dir in dirs:
        try:
            print('\nold_name: ', root_path + dir)
            print('new_name: ', root_path + re.sub(reg_ex, '', dir))
            os.rename(root_path + dir, root_path + re.sub(reg_ex, '', dir))
        except:
            error = error + 1
            print("Exception occured : ", sys.exc_info())

    for file in files:
        try:
            print('\nold_name: ', root_path + file)
            print('new_name: ', root_path + re.sub(reg_ex, '', file))
            os.rename(root_path + file,  root_path + re.sub(reg_ex, '', file))
        except:
            error = error + 1
            print("Exception occured : ", sys.exc_info())

    print("\n ============================================= \n")

if error == 0:
    print("Operations finished succefully !\n")
else:
    print("Operations finished with ", error , " errros !\n")