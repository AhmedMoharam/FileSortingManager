import PySimpleGUI as Sg
import os


def not_valid_file(param):
    return not os.path.isfile(param)


def not_valid_folder(param):
    return not os.path.isdir(param)


class AppView:
    def __init__(self):
        self.tab1_txt = "Organize Files Using Excel Data"
        self.tab1_tip = "Read first sheet of excel file such that column A contains files names to be moved," \
                        " column D contains folders names to be created and move corresponding file to."
        self.tab2_txt = "Organize Files Into Sub-Folders"
        self.tab2_tip = "Move each 100 file in Workspace Folder to sub folders that are numerically ordered. " \
                        "Up to 10k file. Files with similar names and different suffix are counted as 1."
        self.tab3_txt = "Sub-Folders Files Into Workspace Folder"
        self.tab3_tip = "Undo organization into folders by moving files in sub folder of workspace folder " \
                        "to the workspace folder."
        self.window = None
        self.on_tab1_run = None
        self.on_tab2_run = None
        self.on_tab3_run = None

    def construct(self):
        Sg.theme('DefaultNoMoreNagging')

        tab1_layout = [
            [Sg.Text("Excel File:", size=(19, 1)), Sg.In(key='-FILE-'),
             Sg.FileBrowse(file_types=(("xlsx Excel", "*.xlsx"),))],
            [Sg.Text("Workspace Folder:", size=(19, 1)), Sg.In(key='-FOLDER1-'), Sg.FolderBrowse()],
            [Sg.Text("Renaming Prefix (optional):", size=(19, 1)), Sg.In(size=(8, 1), key='-PREFIX-')]
        ]

        tab2_layout = [
            [Sg.Text("Workspace Folder:", size=(8, 1)), Sg.In(key='-FOLDER2-'), Sg.FolderBrowse()]
        ]

        tab3_layout = [
            [Sg.Text("Workspace Folder:", size=(8, 1)), Sg.In(key='-FOLDER3-'), Sg.FolderBrowse()],
        ]

        layout = [
            [Sg.TabGroup([[Sg.Tab(self.tab1_txt, tab1_layout, tooltip=self.tab1_tip),
                           Sg.Tab(self.tab2_txt, tab2_layout, tooltip=self.tab2_tip),
                           Sg.Tab(self.tab3_txt, tab3_layout, tooltip=self.tab3_tip)]])],
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
                    if not values['-FILE-'] or not values['-FOLDER1-']:
                        Sg.popup("please enter a valid excel file path and workspace folder path !")
                    elif not_valid_file(values['-FILE-']):
                        Sg.popup("please enter a valid excel file path !")
                    elif not_valid_folder(values['-FOLDER1-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab1_run is not None:
                            if not values['-PREFIX-']:
                                self.on_tab1_run(values['-FILE-'], values['-FOLDER1-'])
                            else:
                                self.on_tab1_run(values['-FILE-'], values['-FOLDER1-'], values['-PREFIX-'])
                            Sg.popup('Done!')
                elif values[0] == self.tab2_txt:
                    if not values['-FOLDER2-']:
                        Sg.popup("please enter a valid workspace folder path !")
                    elif not_valid_folder(values['-FOLDER2-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab2_run is not None:
                            self.on_tab2_run(values['-FOLDER2-'])
                            Sg.popup('Done!')
                elif values[0] == self.tab3_txt:
                    if not values['-FOLDER3-']:
                        Sg.popup("please enter a valid workspace folder path !")
                    elif not_valid_folder(values['-FOLDER3-']):
                        Sg.popup("please enter a valid workspace folder path !")
                    else:
                        if self.on_tab3_run is not None:
                            self.on_tab3_run(values['-FOLDER3-'])
                            Sg.popup('Done!')
        self.window.close()









