import pandas as pd
import os

from utils import sub_dirs, sub_file, is_empty_dir, is_similar, move_file_to_dir, find


def organize_files_into_sub_folders(files, sub_folders, working_directory, rename_prefix=False):
    cwd = os.getcwd()
    if os.path.isdir(working_directory):
        os.chdir(working_directory)
        for file, sub_folder in zip(files, sub_folders):
            file_path = find(file)
            if file_path is not None:
                move_file_to_dir(file_path, sub_folder, rename_prefix)
                try:
                    basename = os.path.basename(file_path)
                    if '.' in basename:
                        if basename.rpartition('.')[2] == 'eps':
                            similar_file = basename.rpartition('.')[0] + '.jpg'
                            similar_file_path = find(similar_file)
                            if similar_file_path is not None:
                                move_file_to_dir(similar_file_path, sub_folder, rename_prefix)
                        elif basename.rpartition('.')[2] == 'jpg':
                            similar_file = basename.rpartition('.')[0] + '.jpg'
                            similar_file_path = find(similar_file)
                            if similar_file_path is not None:
                                move_file_to_dir(similar_file_path, sub_folder, rename_prefix)
                except:
                    pass
        os.chdir(cwd)


def organize_files_using_excel_data(excel_file_path, working_directory, rename_prefix=False):
    xlsx = pd.ExcelFile(excel_file_path)
    sheet = xlsx.parse(0)
    col_a_heading = sheet.keys()[0]
    col_d_heading = sheet.keys()[3]
    organize_files_into_sub_folders(sheet[col_a_heading], sheet[col_d_heading], working_directory, rename_prefix)


def disorganize_files_from_directory_sub_folders(working_directory):
    if os.path.isdir(working_directory):
        for sub_folder in sub_dirs(working_directory):
            for file in sub_file(os.path.join(working_directory, sub_folder)):
                move_file_to_dir(os.path.join(working_directory, sub_folder, file), working_directory)
            if is_empty_dir(os.path.join(working_directory, sub_folder)):
                os.rmdir(os.path.join(working_directory, sub_folder))


def organize_each_hundred_file_in_sub_folders(working_directory):
    if not os.path.isdir(working_directory):
        return
    dir_count = 0
    count = 0
    last_file = ""
    current_directory_name = str(dir_count).zfill(3)
    for file in sorted(sub_file(working_directory)):
        if not is_similar(file, last_file):
            if count < 100:
                count += 1
            else:
                count = 1
                dir_count += 1
                current_directory_name = str(dir_count).zfill(3)
        move_file_to_dir(os.path.join(working_directory, file),
                         os.path.join(working_directory, current_directory_name))
        last_file = file


def main():
    organize_files_using_excel_data("tc\\Book1.xlsx", "tc\\Root_dir")
    disorganize_files_from_directory_sub_folders("tc\\Root_dir")
    organize_each_hundred_file_in_sub_folders("tc\\Root_dir")
    disorganize_files_from_directory_sub_folders("tc\\Root_dir")
    #touch_files("tc\\Root_dir", 10000)


if __name__ == "__main__":
    main()
