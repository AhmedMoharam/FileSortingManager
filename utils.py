import os
import shutil
from random import randint


def is_nan(x):
    return x != x


def sub_dirs(path):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            yield entry.name


def sub_file(path):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_file():
            yield entry.name


def is_empty_dir(path):
    if os.listdir(path):
        return False
    else:
        return True


def is_similar(file1, file2):
    if '.' in file1 and '.' in file2:
        return file1.rpartition('.')[0] == file2.rpartition('.')[0]
    else:
        return False


def move_file_to_dir(file, directory: str, rename_prefix=False):
    try:
        basename = os.path.basename(file)
        if rename_prefix:
            new_file_name = str(randint(000, 999)).zfill(3) + '_' + basename
        else:
            new_file_name = basename

        if os.path.isfile(os.path.join(directory, new_file_name)):
            return

        if not os.path.isdir(directory):
            os.mkdir(directory)

        shutil.move(file, os.path.join(directory, new_file_name))
    except:
        move_file_to_dir(file, 'Unsorted', rename_prefix)
        pass


def find(name, path='.'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def touch_files(working_directory, count):
    for i in range(count):
        open(os.path.join(working_directory, str(i).zfill(5)), 'a').close()