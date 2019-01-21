import os
import shutil
import sys

def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)

def rem_file(full_name):
    try:
        if full_name.endswith(".backup"):
        	os.remove(full_name)
    except:
        print(dir_path + ' - такого файла нет')
 
first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file, backup_file)
full_name = os.path.join(os.getcwd(), backup_file)
rem_file (full_name)
