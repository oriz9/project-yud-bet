import Mongodb_A
import PySimpleGUI as sg
import time
import first_UI

sg.theme('Dark')  # Add a touch of col

add_account_lay = [[sg.Text("name:")], [sg.InputText()],
                   [sg.Text("password")], [sg.InputText()],
                   [sg.Text("folderr accsess")],
                   [sg.Checkbox("program", key="program")],
                   [sg.Checkbox("bills", key="bills")],
                   [sg.Button("add account")], [sg.Button("back")], [sg.Exit()]]


def adding_account_ui():
    window = sg.Window('add account menu', add_account_lay)
    folder_place = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        if event == "back":
            window.close()
            admin_panel_ui()
        print(values[0])
        for x in values:
            if type(values[x]) == bool and values[x]:
                folder_place = folder_place + ", " + x

        account = {"name": values[0], "password": values[1], "folder": folder_place}
        print(account)
        Mongodb_A.addd_account(account)
    window.close()


# -------------------------------------------------------------------------------------------------

login_admin_lay = [[sg.Button("add account")],
                   [sg.Button("show folder")], ]


def admin_panel_ui():
    window = sg.Window('admin menu', login_admin_lay)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

        if event == "add account":
            window.close()
            adding_account_ui()
        elif event == "show folder":
            window.close()
            first_UI.file_explorer_gui()
    window.close()