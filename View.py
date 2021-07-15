import PySimpleGUI as Sg
import os


def not_valid_file(param):
    return not os.path.isfile(param)


def not_valid_folder(param):
    return not os.path.isdir(param)


class AppView:
    def __init__(self):
        self.tab1_txt = "Preparing files"
        self.tab1_tip = "Read first sheet of excel file such that column A contains files names to be moved,\n" \
                        "column D contains folders names to be created and move corresponding file to.\n" \
                        "Adding random prefix of 3 digits before each moved file."
        self.tab2_txt = "Sort 100s"
        self.tab2_tip = "Move each 100 file in Workspace Folder to sub folders that are numerically ordered.\n" \
                        "Up to 10k file.\nFiles with similar names and different suffix are counted as 1."
        self.tab3_txt = "Group files"
        self.tab3_tip = "Undo organization into folders by moving files in sub folder of workspace folder " \
                        "to the workspace folder."
        self.tab4_txt = "Rejected files"
        self.tab4_tip = "Read first sheet of excel file such that column A contains files names to be moved,\n" \
                        "column D contains folders names to be created and move corresponding file to."
        self.window = None
        self.on_tab1_run = None
        self.on_tab2_run = None
        self.on_tab3_run = None

    def construct(self):
        Sg.theme('DefaultNoMoreNagging')

        tab1_layout = [
            [Sg.Text("Excel File:", size=(8, 1)), Sg.In(key='-FILE1-'),
             Sg.FileBrowse(file_types=(("xlsx Excel", "*.xlsx"),))],
            [Sg.Text("Folder:", size=(8, 1)), Sg.In(key='-FOLDER1-'), Sg.FolderBrowse()]
        ]

        tab2_layout = [
            [Sg.Text("Folder:", size=(8, 1)), Sg.In(key='-FOLDER2-'), Sg.FolderBrowse()]
        ]

        tab3_layout = [
            [Sg.Text("Folder:", size=(8, 1)), Sg.In(key='-FOLDER3-'), Sg.FolderBrowse()],
        ]

        tab4_layout = [
            [Sg.Text("Excel File:", size=(8, 1)), Sg.In(key='-FILE4-'),
             Sg.FileBrowse(file_types=(("xlsx Excel", "*.xlsx"),))],
            [Sg.Text("Folder:", size=(8, 1)), Sg.In(key='-FOLDER4-'), Sg.FolderBrowse()]
        ]

        layout = [
            [Sg.TabGroup([[Sg.Tab(self.tab1_txt, tab1_layout, tooltip=self.tab1_tip),
                           Sg.Tab(self.tab2_txt, tab2_layout, tooltip=self.tab2_tip),
                           Sg.Tab(self.tab3_txt, tab3_layout, tooltip=self.tab3_tip),
                           Sg.Tab(self.tab4_txt, tab4_layout, tooltip=self.tab4_tip)]])],
            [Sg.Button("Run", key='-Run-'), Sg.Button("Cancel", key='-Cancel-')]
        ]
        self.window = Sg.Window('File Sorting Manager', layout)

    def set_call_backs(self, tab1_run_cb, tab2_run_cb, tab3_run_cb):
        self.on_tab1_run = tab1_run_cb
        self.on_tab2_run = tab2_run_cb
        self.on_tab3_run = tab3_run_cb

    def run(self):
        while True:
            event, values = self.window.read()
            if event == Sg.WIN_CLOSED or event == '-Cancel-':  # always,  always give a way out!
                break
            elif event == '-Run-':
                if values[0] == self.tab1_txt:
                    if not values['-FILE1-'] or not values['-FOLDER1-']:
                        Sg.popup("please enter a valid excel file path and workspace folder path !")
                    elif not_valid_file(values['-FILE1-']):
                        Sg.popup("please enter a valid excel file path !")
                    elif not_valid_folder(values['-FOLDER1-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab1_run is not None:
                            self.on_tab1_run(values['-FILE1-'], values['-FOLDER1-'], True)
                            self.window['-FILE1-']('')
                            self.window['-FOLDER1-']('')
                            Sg.popup('Done!')
                elif values[0] == self.tab2_txt:
                    if not values['-FOLDER2-']:
                        Sg.popup("please enter a valid workspace folder path !")
                    elif not_valid_folder(values['-FOLDER2-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab2_run is not None:
                            self.on_tab2_run(values['-FOLDER2-'])
                            self.window['-FOLDER2-']('')
                            Sg.popup('Done!')
                elif values[0] == self.tab3_txt:
                    if not values['-FOLDER3-']:
                        Sg.popup("please enter a valid workspace folder path !")
                    elif not_valid_folder(values['-FOLDER3-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab3_run is not None:
                            self.on_tab3_run(values['-FOLDER3-'])
                            self.window['-FOLDER3-']('')
                            Sg.popup('Done!')
                elif values[0] == self.tab4_txt:
                    if not values['-FILE4-'] or not values['-FOLDER4-']:
                        Sg.popup("please enter a valid excel file path and workspace folder path !")
                    elif not_valid_file(values['-FILE4-']):
                        Sg.popup("please enter a valid excel file path !")
                    elif not_valid_folder(values['-FOLDER4-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab1_run is not None:
                            self.on_tab1_run(values['-FILE4-'], values['-FOLDER4-'])
                            self.window['-FILE4-']('')
                            self.window['-FOLDER4-']('')
                            Sg.popup('Done!')
        self.window.close()









