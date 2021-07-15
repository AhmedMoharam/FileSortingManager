from View import AppView
from Model import organize_files_using_excel_data, \
    disorganize_files_from_directory_sub_folders, organize_each_hundred_file_in_sub_folders


def main():
    my_app_view = AppView()
    my_app_view.construct()
    my_app_view.set_call_backs(organize_files_using_excel_data,
                               organize_each_hundred_file_in_sub_folders,
                               disorganize_files_from_directory_sub_folders)
    my_app_view.run()


if __name__ == "__main__":
    main()
