from importlib.resources import path
import os
import re
import sys

list = []
PATH = './dir1/'
reg_ex = r'[0-9_:]'

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
    
    for dir in dirs:
        root_path = root
        if root != PATH:
            root_path = root + "/"
        try:
            print('\nold_name: ', root_path + dir)
            print('new_name: ', root_path + re.sub(reg_ex, '', dir))
            os.rename(root_path + dir, root_path + re.sub(reg_ex, '', dir))
        except:
            print("Exception occured : ", sys.exc_info())

    for file in files:
        root_path = root
        if root != PATH:
            root_path = root + "/"
        try:
            print('\nold_name: ', root_path + file)
            print('new_name: ', root_path + re.sub(reg_ex, '', file))
            os.rename(root_path + file,  root_path + re.sub(reg_ex, '', file))
        except:
            print("Exception occured : ", sys.exc_info())
    print("\n ============================================= \n")

# txt = 'Man:de/ana ve ny ma:nd_e r:a/ atao an\'zao?'
# print(re.sub(reg_ex, '', txt))